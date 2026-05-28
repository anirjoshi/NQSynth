import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & Eq(delta + skoX + 1, 0) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2)) | ((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & Eq(delta - skoX - 1, 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2)) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= -1) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoX <= 1) & (-delta - skoS2**2 <= -2)) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoX < 1) & (-delta - skoS2**2 <= -2) & ((-delta + skoX < -1) | Eq(delta - skoX - 1, 0))) | ((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (delta - skoX < 1) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((-delta + skoX <= -1) | (delta - skoX <= 1))) | ((skoX < 1) & (-skoS2 <= 0) & (-delta < 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (delta - skoX < 1) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((delta - skoX < 1) | Eq(delta - skoX - 1, 0))) | ((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoX < 1) & (-delta - skoS2**2 <= -2) & ((delta + skoX <= -1) | (-delta - skoX <= 1))) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & Eq(delta + skoX + 1, 0) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoX < 1) & (-delta - skoS2**2 <= -2) & ((-delta < 0) | (Eq(delta, 0) & Eq(delta + skoX + 1, 0)))) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (delta - skoX < 1) & Eq(delta - skoX - 1, 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((-delta < 0) | (Eq(delta, 0) & (delta - skoX < 1))))

	pre_cond = Or(And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(-1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(-1)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Integer(0)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(-1)), LessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(1)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Integer(0)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(LessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(-1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(1)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), And(Equality(Symbol('delta'), Integer(0)), Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(1)), Integer(0))))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(1)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), And(Equality(Symbol('delta'), Integer(0)), StrictLessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(1))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & Eq(delta + skoX - 1, 0) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2)) | ((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & Eq(delta - skoX + 1, 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2)) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (-delta + skoX <= 1) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= -1) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2)) | ((skoX < 1) & (-skoS2 <= 0) & (-delta < 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (delta + skoX < 1) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((delta + skoX < 1) | Eq(delta + skoX - 1, 0))) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (-delta + skoX < 1) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & (Eq(delta + skoX - 1, 0) | (-delta - skoX < -1))) | ((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (delta + skoX < 1) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((delta + skoX <= 1) | (-delta - skoX <= -1))) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (delta + skoX < 1) & Eq(delta + skoX - 1, 0) & (-delta + skoX <= 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((-delta < 0) | (Eq(delta, 0) & (delta + skoX < 1)))) | ((skoX < 1) & (-delta <= 0) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (-delta + skoX < 1) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((-delta + skoX <= 1) | (delta - skoX <= -1))) | ((skoX < 1) & (-skoS2 <= 0) & (-5000000*pi < -15707963) & (10000000*pi < 31415927) & (-skoX < 0) & (-delta + skoX <= 0) & (-delta + skoX < 1) & Eq(delta - skoX + 1, 0) & (-delta + skoS2**2 <= 2) & (-delta - skoX <= 0) & (-delta - skoS2**2 <= -2) & ((-delta < 0) | (Eq(delta, 0) & Eq(delta - skoX + 1, 0))))

	pre_cond = Or(And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(-1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1)), Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(-1)), Integer(0)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(-1)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(LessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(-1)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1)), Equality(Add(Symbol('delta'), Symbol('skoX'), Integer(-1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), And(Equality(Symbol('delta'), Integer(0)), StrictLessThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1))))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(1)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(1)), LessThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1)))), And(StrictLessThan(Symbol('skoX'), Integer(1)), LessThan(Mul(Integer(-1), Symbol('skoS2')), Integer(0)), StrictLessThan(Mul(Integer(-1), Integer(5000000), Symbol('pi')), Integer(-15707963)), StrictLessThan(Mul(Integer(10000000), Symbol('pi')), Integer(31415927)), StrictLessThan(Mul(Integer(-1), Symbol('skoX')), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('delta')), Symbol('skoX')), Integer(1)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2))), Integer(2)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Symbol('skoX'))), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Integer(-2)), Or(StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), And(Equality(Symbol('delta'), Integer(0)), Equality(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Integer(0))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (0 <= skoS2) & (0 <= skoSM) & (0 <= skoSP) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoX:sympy.Rational=None, skoS2:sympy.Rational=None, pi:sympy.Rational=None, skoSP:sympy.Rational=None, skoSM:sympy.Rational=None):
	assert delta!=None
	assert skoX!=None
	assert skoS2!=None
	assert pi!=None


	if skoSP==None:
		assert skoSM!=None
		return lambda skoSP: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)

	if skoSM==None:
		assert skoSP!=None
		return lambda skoSM: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)


	return post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)


def get_univariate_poly( delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoS2')), LessThan(Integer(0), Symbol('skoSM')), LessThan(Integer(0), Symbol('skoSP')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoX:\n"))
	ip_1=int(input("enter denominator of skoX:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoX=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoS2:\n"))
	ip_1=int(input("enter denominator of skoS2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS2=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of pi:\n"))
	ip_1=int(input("enter denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['skoSM'] = Integer(1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Integer(1)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Integer(1))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
