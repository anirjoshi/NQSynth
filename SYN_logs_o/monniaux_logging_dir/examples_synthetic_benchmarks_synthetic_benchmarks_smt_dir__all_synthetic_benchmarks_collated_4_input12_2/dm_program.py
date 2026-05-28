import sympy
from sympy import *

def pre_condition_0(r:sympy.Rational,c:sympy.Rational):
	#(-3*c + l**2 + r + 1/4 < 0) & (l**2 - r**2 + 1/4 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Integer(3), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 4)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 4)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 17/64) & (3*c - r > 17/64)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(17, 64)), StrictGreaterThan(Add(Mul(Integer(3), Symbol('c')), Mul(Integer(-1), Symbol('r'))), Rational(17, 64)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r:sympy.Rational,c:sympy.Rational):
	#(2*c + l**2 + r + 4 < 0) & (l**2 - r**2 + 4 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Integer(4)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Integer(4)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 8) & (2*c + r < -8)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Integer(8)), StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Symbol('r')), Integer(-8)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r:sympy.Rational,c:sympy.Rational):
	#(-2*c + l**2 + r < 0) & (l**2 - r**2 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Integer(2), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r')), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 0) & (r < 2*c)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Integer(0)), StrictLessThan(Symbol('r'), Mul(Integer(2), Symbol('c'))))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r:sympy.Rational,c:sympy.Rational):
	#(-4385*c/2048 + l**2 + r + 83521/16777216 < 0) & (l**2 - r**2 + 83521/16777216 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4385, 2048), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(83521, 16777216)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(83521, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 83521/16777216) & (4385*c - 2048*r > 83521/8192)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(83521, 16777216)), StrictGreaterThan(Add(Mul(Integer(4385), Symbol('c')), Mul(Integer(-1), Integer(2048), Symbol('r'))), Rational(83521, 8192)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r:sympy.Rational,c:sympy.Rational):
	#(-61*c/32 + l**2 + r + 9/4096 < 0) & (l**2 - r**2 + 9/4096 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(61, 32), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(9, 4096)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(9, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 9/4096) & (61*c - 32*r > 9/128)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(9, 4096)), StrictGreaterThan(Add(Mul(Integer(61), Symbol('c')), Mul(Integer(-1), Integer(32), Symbol('r'))), Rational(9, 128)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r:sympy.Rational,c:sympy.Rational):
	#(-967952859276900506917345671511858171389412015131275481253*c/484040407824903873290622868807986378669738769531250000000 + l**2 + r + 16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009/937180465629197051229621782290090609488529244964716632829496156809057083592051640152931213378906250000000000000000 < 0) & (l**2 - r**2 + 16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009/937180465629197051229621782290090609488529244964716632829496156809057083592051640152931213378906250000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(967952859276900506917345671511858171389412015131275481253, 484040407824903873290622868807986378669738769531250000000), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009, 937180465629197051229621782290090609488529244964716632829496156809057083592051640152931213378906250000000000000000)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009, 937180465629197051229621782290090609488529244964716632829496156809057083592051640152931213378906250000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009/937180465629197051229621782290090609488529244964716632829496156809057083592051640152931213378906250000000000000000) & (967952859276900506917345671511858171389412015131275481253*c - 484040407824903873290622868807986378669738769531250000000*r > 16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009/1936161631299615493162491475231945514678955078125000000000)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009, 937180465629197051229621782290090609488529244964716632829496156809057083592051640152931213378906250000000000000000)), StrictGreaterThan(Add(Mul(Integer(967952859276900506917345671511858171389412015131275481253), Symbol('c')), Mul(Integer(-1), Integer(484040407824903873290622868807986378669738769531250000000), Symbol('r'))), Rational(16372833367576576677387466238858288664513942257304066499706177675376341592989049398724762823677581754450009, 1936161631299615493162491475231945514678955078125000000000)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r:sympy.Rational,c:sympy.Rational):
	#(-16383*c/8192 + l**2 + r + 1/268435456 < 0) & (l**2 - r**2 + 1/268435456 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(16383, 8192), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 268435456)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 268435456)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/268435456) & (16383*c - 8192*r > 1/32768)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 268435456)), StrictGreaterThan(Add(Mul(Integer(16383), Symbol('c')), Mul(Integer(-1), Integer(8192), Symbol('r'))), Rational(1, 32768)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(r:sympy.Rational,c:sympy.Rational):
	#(-65535*c/32768 + l**2 + r + 1/4294967296 < 0) & (l**2 - r**2 + 1/4294967296 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(65535, 32768), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 4294967296)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 5/17179869184) & (65535*c - 32768*r > 5/524288)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(5, 17179869184)), StrictGreaterThan(Add(Mul(Integer(65535), Symbol('c')), Mul(Integer(-1), Integer(32768), Symbol('r'))), Rational(5, 524288)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(r:sympy.Rational,c:sympy.Rational):
	#(-131071*c/65536 + l**2 + r + 1/17179869184 < 0) & (l**2 - r**2 + 1/17179869184 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(131071, 65536), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 17179869184)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/17179869184) & (131071*c - 65536*r > 1/262144)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 17179869184)), StrictGreaterThan(Add(Mul(Integer(131071), Symbol('c')), Mul(Integer(-1), Integer(65536), Symbol('r'))), Rational(1, 262144)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(r:sympy.Rational,c:sympy.Rational):
	#(-262143*c/131072 + l**2 + r + 1/68719476736 < 0) & (l**2 - r**2 + 1/68719476736 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(262143, 131072), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 68719476736)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 68719476736)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/68719476736) & (262143*c - 131072*r > 1/524288)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 68719476736)), StrictGreaterThan(Add(Mul(Integer(262143), Symbol('c')), Mul(Integer(-1), Integer(131072), Symbol('r'))), Rational(1, 524288)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(r:sympy.Rational,c:sympy.Rational):
	#(-524287*c/262144 + l**2 + r + 1/274877906944 < 0) & (l**2 - r**2 + 1/274877906944 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(524287, 262144), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 274877906944)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 274877906944)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/274877906944) & (524287*c - 262144*r > 1/1048576)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 274877906944)), StrictGreaterThan(Add(Mul(Integer(524287), Symbol('c')), Mul(Integer(-1), Integer(262144), Symbol('r'))), Rational(1, 1048576)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(r:sympy.Rational,c:sympy.Rational):
	#(-1048575*c/524288 + l**2 + r + 1/1099511627776 < 0) & (l**2 - r**2 + 1/1099511627776 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(1048575, 524288), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 1099511627776)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 1099511627776)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/1099511627776) & (1048575*c - 524288*r > 1/2097152)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 1099511627776)), StrictGreaterThan(Add(Mul(Integer(1048575), Symbol('c')), Mul(Integer(-1), Integer(524288), Symbol('r'))), Rational(1, 2097152)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(r:sympy.Rational,c:sympy.Rational):
	#(-4194303*c/2097152 + l**2 + r + 1/17592186044416 < 0) & (l**2 - r**2 + 1/17592186044416 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4194303, 2097152), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 17592186044416)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 17592186044416)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/17592186044416) & (4194303*c - 2097152*r > 1/8388608)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 17592186044416)), StrictGreaterThan(Add(Mul(Integer(4194303), Symbol('c')), Mul(Integer(-1), Integer(2097152), Symbol('r'))), Rational(1, 8388608)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(r:sympy.Rational,c:sympy.Rational):
	#(-8388607*c/4194304 + l**2 + r + 1/70368744177664 < 0) & (l**2 - r**2 + 1/70368744177664 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(8388607, 4194304), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 70368744177664)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 70368744177664)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/70368744177664) & (8388607*c - 4194304*r > 1/16777216)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 70368744177664)), StrictGreaterThan(Add(Mul(Integer(8388607), Symbol('c')), Mul(Integer(-1), Integer(4194304), Symbol('r'))), Rational(1, 16777216)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(r:sympy.Rational,c:sympy.Rational):
	#(-16777215*c/8388608 + l**2 + r + 1/281474976710656 < 0) & (l**2 - r**2 + 1/281474976710656 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(16777215, 8388608), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 281474976710656)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 281474976710656)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/281474976710656) & (16777215*c - 8388608*r > 1/33554432)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 281474976710656)), StrictGreaterThan(Add(Mul(Integer(16777215), Symbol('c')), Mul(Integer(-1), Integer(8388608), Symbol('r'))), Rational(1, 33554432)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(r:sympy.Rational,c:sympy.Rational):
	#(-33554431*c/16777216 + l**2 + r + 1/1125899906842624 < 0) & (l**2 - r**2 + 1/1125899906842624 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(33554431, 16777216), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 1125899906842624)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 1125899906842624)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/1125899906842624) & (33554431*c - 16777216*r > 1/67108864)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 1125899906842624)), StrictGreaterThan(Add(Mul(Integer(33554431), Symbol('c')), Mul(Integer(-1), Integer(16777216), Symbol('r'))), Rational(1, 67108864)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(r:sympy.Rational,c:sympy.Rational):
	#(-67108863*c/33554432 + l**2 + r + 1/4503599627370496 < 0) & (l**2 - r**2 + 1/4503599627370496 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(67108863, 33554432), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 4503599627370496)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 4503599627370496)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/4503599627370496) & (67108863*c - 33554432*r > 1/134217728)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 4503599627370496)), StrictGreaterThan(Add(Mul(Integer(67108863), Symbol('c')), Mul(Integer(-1), Integer(33554432), Symbol('r'))), Rational(1, 134217728)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(r:sympy.Rational,c:sympy.Rational):
	#(-134217727*c/67108864 + l**2 + r + 1/18014398509481984 < 0) & (l**2 - r**2 + 1/18014398509481984 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(134217727, 67108864), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(1, 18014398509481984)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(1, 18014398509481984)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 1/18014398509481984) & (134217727*c - 67108864*r > 1/268435456)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1, 18014398509481984)), StrictGreaterThan(Add(Mul(Integer(134217727), Symbol('c')), Mul(Integer(-1), Integer(67108864), Symbol('r'))), Rational(1, 268435456)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(r:sympy.Rational,c:sympy.Rational):
	#(-5592405187500000620881716410319*c/2796202625000000000000000000000 + l**2 + r + 3906249922389785834204230772623785823169681761/31274996480227562500000000000000000000000000000000000000000000 < 0) & (l**2 - r**2 + 3906249922389785834204230772623785823169681761/31274996480227562500000000000000000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(5592405187500000620881716410319, 2796202625000000000000000000000), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3906249922389785834204230772623785823169681761, 31274996480227562500000000000000000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3906249922389785834204230772623785823169681761, 31274996480227562500000000000000000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3906249922389785834204230772623785823169681761/31274996480227562500000000000000000000000000000000000000000000) & (5592405187500000620881716410319*c - 2796202625000000000000000000000*r > 3906249922389785834204230772623785823169681761/11184810500000000000000000000000)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3906249922389785834204230772623785823169681761, 31274996480227562500000000000000000000000000000000000000000000)), StrictGreaterThan(Add(Mul(Integer(5592405187500000620881716410319), Symbol('c')), Mul(Integer(-1), Integer(2796202625000000000000000000000), Symbol('r'))), Rational(3906249922389785834204230772623785823169681761, 11184810500000000000000000000000)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(r:sympy.Rational,c:sympy.Rational):
	#(-238609284888888950149218167358831*c/119304644000000000000000000000000 + l**2 + r + 9679011964503633921360649183104828097294313686561/56934392319866944000000000000000000000000000000000000000000000000 < 0) & (l**2 - r**2 + 9679011964503633921360649183104828097294313686561/56934392319866944000000000000000000000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(238609284888888950149218167358831, 119304644000000000000000000000000), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(9679011964503633921360649183104828097294313686561, 56934392319866944000000000000000000000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(9679011964503633921360649183104828097294313686561, 56934392319866944000000000000000000000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 9679011964503633921360649183104828097294313686561/56934392319866944000000000000000000000000000000000000000000000000) & (238609284888888950149218167358831*c - 119304644000000000000000000000000*r > 9679011964503633921360649183104828097294313686561/477218576000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(9679011964503633921360649183104828097294313686561, 56934392319866944000000000000000000000000000000000000000000000000)), StrictGreaterThan(Add(Mul(Integer(238609284888888950149218167358831), Symbol('c')), Mul(Integer(-1), Integer(119304644000000000000000000000000), Symbol('r'))), Rational(9679011964503633921360649183104828097294313686561, 477218576000000000000000000000000)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(r:sympy.Rational,c:sympy.Rational):
	#(-1908874252444445870977942109353697*c/954437139555555840000000000000000 + l**2 + r + 711111065370066045277633344795248018261379047567809/3643801013451966297109303245432422400000000000000000000000000000000 < 0) & (l**2 - r**2 + 711111065370066045277633344795248018261379047567809/3643801013451966297109303245432422400000000000000000000000000000000 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(1908874252444445870977942109353697, 954437139555555840000000000000000), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(711111065370066045277633344795248018261379047567809, 3643801013451966297109303245432422400000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(711111065370066045277633344795248018261379047567809, 3643801013451966297109303245432422400000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 711111065370066045277633344795248018261379047567809/3643801013451966297109303245432422400000000000000000000000000000000) & (1908874252444445870977942109353697*c - 954437139555555840000000000000000*r > 711111065370066045277633344795248018261379047567809/3817748558222223360000000000000000)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(711111065370066045277633344795248018261379047567809, 3643801013451966297109303245432422400000000000000000000000000000000)), StrictGreaterThan(Add(Mul(Integer(1908874252444445870977942109353697), Symbol('c')), Mul(Integer(-1), Integer(954437139555555840000000000000000), Symbol('r'))), Rational(711111065370066045277633344795248018261379047567809, 3817748558222223360000000000000000)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(r:sympy.Rational,c:sympy.Rational):
	#(r**2 > 3969/18446744073709551616) & (4294967233*c - 2147483648*r > 3969/8589934592)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(3969, 18446744073709551616)), StrictGreaterThan(Add(Mul(Integer(4294967233), Symbol('c')), Mul(Integer(-1), Integer(2147483648), Symbol('r'))), Rational(3969, 8589934592)))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(r:sympy.Rational,c:sympy.Rational):
	#(-4294967233*c/2147483648 + l**2 + r + 3969/18446744073709551616 < 0) & (l**2 - r**2 + 3969/18446744073709551616 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Rational(4294967233, 2147483648), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Rational(3969, 18446744073709551616)), Integer(0)), StrictLessThan(Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Rational(3969, 18446744073709551616)), Integer(0)))