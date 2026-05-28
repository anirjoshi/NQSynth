import sympy
from sympy import *

def pre_condition_0(y:sympy.Rational):
	#((y > sqrt(199335)/200) | (y > -sqrt(319)/8)) & ((y > sqrt(199335)/200) | (y < -sqrt(199335)/200)) & ((y > -sqrt(319)/8) | (y < sqrt(319)/8)) & ((y < -sqrt(199335)/200) | (y < sqrt(319)/8))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 200), Pow(Integer(199335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(319), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 200), Pow(Integer(199335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 200), Pow(Integer(199335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(319), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 200), Pow(Integer(199335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(319), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(y:sympy.Rational):
	#((y > sqrt(2505535)/12800) | (y > -sqrt(4271)/512)) & ((y > sqrt(2505535)/12800) | (y < -sqrt(2505535)/12800)) & ((y > -sqrt(4271)/512) | (y < sqrt(4271)/512)) & ((y < -sqrt(2505535)/12800) | (y < sqrt(4271)/512))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(2505535), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(4271), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(2505535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(2505535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(4271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(4271), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(2505535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(4271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(y:sympy.Rational):
	#((y > sqrt(10485697935)/51200) | (y > -sqrt(16781311)/2048)) & ((y > sqrt(10485697935)/51200) | (y < -sqrt(10485697935)/51200)) & ((y > -sqrt(16781311)/2048) | (y < sqrt(16781311)/2048)) & ((y < -sqrt(10485697935)/51200) | (y < sqrt(16781311)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10485697935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16781311), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10485697935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10485697935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16781311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16781311), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10485697935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16781311), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(y:sympy.Rational):
	#((y > sqrt(46239135)/3200) | (y > -sqrt(73999)/128)) & ((y > sqrt(46239135)/3200) | (y < -sqrt(46239135)/3200)) & ((y > -sqrt(73999)/128) | (y < sqrt(73999)/128)) & ((y < -sqrt(46239135)/3200) | (y < sqrt(73999)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(46239135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(46239135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(46239135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73999), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(46239135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(y:sympy.Rational):
	#((y > sqrt(10485513615)/102400) | (y > -sqrt(16793599)/4096)) & ((y > sqrt(10485513615)/102400) | (y < -sqrt(10485513615)/102400)) & ((y > -sqrt(16793599)/4096) | (y < sqrt(16793599)/4096)) & ((y < -sqrt(10485513615)/102400) | (y < sqrt(16793599)/4096))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(10485513615), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(16793599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(10485513615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(10485513615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(16793599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(16793599), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(10485513615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(16793599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(y:sympy.Rational):
	#((y > 3*sqrt(3838735)/102400) | (y > -sqrt(72055)/4096)) & ((y > 3*sqrt(3838735)/102400) | (y < -3*sqrt(3838735)/102400)) & ((y > -sqrt(72055)/4096) | (y < sqrt(72055)/4096)) & ((y < -3*sqrt(3838735)/102400) | (y < sqrt(72055)/4096))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 102400), Pow(Integer(3838735), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(72055), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 102400), Pow(Integer(3838735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 102400), Pow(Integer(3838735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(72055), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(72055), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 102400), Pow(Integer(3838735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(72055), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(y:sympy.Rational):
	#((y > sqrt(174233415)/6400) | (y > -sqrt(278839)/256)) & ((y > sqrt(174233415)/6400) | (y < -sqrt(174233415)/6400)) & ((y > -sqrt(278839)/256) | (y < sqrt(278839)/256)) & ((y < -sqrt(174233415)/6400) | (y < sqrt(278839)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(174233415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(278839), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(174233415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(174233415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(278839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(278839), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(174233415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(278839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(y:sympy.Rational):
	#((y > sqrt(2703739015)/25600) | (y > -sqrt(4327031)/1024)) & ((y > sqrt(2703739015)/25600) | (y < -sqrt(2703739015)/25600)) & ((y > -sqrt(4327031)/1024) | (y < sqrt(4327031)/1024)) & ((y < -sqrt(2703739015)/25600) | (y < sqrt(4327031)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2703739015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4327031), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2703739015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2703739015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4327031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4327031), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2703739015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4327031), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(y:sympy.Rational):
	#(y > -sqrt(31831)/8192) & (y < sqrt(31831)/8192)

	pre_cond = And(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(31831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(31831), Rational(1, 2)))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(y:sympy.Rational):
	#((y > sqrt(2662344015)/25600) | (y > -sqrt(4260799)/1024)) & ((y > sqrt(2662344015)/25600) | (y < -sqrt(2662344015)/25600)) & ((y > -sqrt(4260799)/1024) | (y < sqrt(4260799)/1024)) & ((y < -sqrt(2662344015)/25600) | (y < sqrt(4260799)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2662344015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4260799), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2662344015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2662344015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4260799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4260799), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2662344015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4260799), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(y:sympy.Rational):
	#((y > sqrt(22937935)/51200) | (y > -sqrt(40895)/2048)) & ((y > sqrt(22937935)/51200) | (y < -sqrt(22937935)/51200)) & ((y > -sqrt(40895)/2048) | (y < sqrt(40895)/2048)) & ((y < -sqrt(22937935)/51200) | (y < sqrt(40895)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(22937935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(40895), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(22937935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(22937935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(40895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(40895), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(22937935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(40895), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(y:sympy.Rational):
	#((y > sqrt(481366335)/204800) | (y > -sqrt(837295)/8192)) & ((y > sqrt(481366335)/204800) | (y < -sqrt(481366335)/204800)) & ((y > -sqrt(837295)/8192) | (y < sqrt(837295)/8192)) & ((y < -sqrt(481366335)/204800) | (y < sqrt(837295)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(481366335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(837295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(481366335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(481366335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(837295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(837295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(481366335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(837295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(y:sympy.Rational):
	#((y > 3*sqrt(1174104215)/51200) | (y > -sqrt(16911295)/2048)) & ((y > 3*sqrt(1174104215)/51200) | (y < -3*sqrt(1174104215)/51200)) & ((y > -sqrt(16911295)/2048) | (y < sqrt(16911295)/2048)) & ((y < -3*sqrt(1174104215)/51200) | (y < sqrt(16911295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1174104215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16911295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1174104215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1174104215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16911295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16911295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1174104215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16911295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(y:sympy.Rational):
	#((y > 3*sqrt(1178564215)/51200) | (y > -sqrt(16975519)/2048)) & ((y > 3*sqrt(1178564215)/51200) | (y < -3*sqrt(1178564215)/51200)) & ((y > -sqrt(16975519)/2048) | (y < sqrt(16975519)/2048)) & ((y < -3*sqrt(1178564215)/51200) | (y < sqrt(16975519)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1178564215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16975519), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1178564215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1178564215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16975519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16975519), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1178564215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16975519), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(y:sympy.Rational):
	#((y > sqrt(10526477935)/51200) | (y > -sqrt(16846559)/2048)) & ((y > sqrt(10526477935)/51200) | (y < -sqrt(10526477935)/51200)) & ((y > -sqrt(16846559)/2048) | (y < sqrt(16846559)/2048)) & ((y < -sqrt(10526477935)/51200) | (y < sqrt(16846559)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10526477935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16846559), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10526477935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10526477935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16846559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16846559), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10526477935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16846559), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(y:sympy.Rational):
	#((y > sqrt(10587047935)/51200) | (y > -sqrt(16943471)/2048)) & ((y > sqrt(10587047935)/51200) | (y < -sqrt(10587047935)/51200)) & ((y > -sqrt(16943471)/2048) | (y < sqrt(16943471)/2048)) & ((y < -sqrt(10587047935)/51200) | (y < sqrt(16943471)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10587047935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16943471), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10587047935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10587047935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16943471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16943471), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10587047935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16943471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(y:sympy.Rational):
	#((y > sqrt(10546747935)/51200) | (y > -sqrt(16878991)/2048)) & ((y > sqrt(10546747935)/51200) | (y < -sqrt(10546747935)/51200)) & ((y > -sqrt(16878991)/2048) | (y < sqrt(16878991)/2048)) & ((y < -sqrt(10546747935)/51200) | (y < sqrt(16878991)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10546747935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16878991), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10546747935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10546747935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16878991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16878991), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10546747935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16878991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(y:sympy.Rational):
	#((y > 3*sqrt(295264335)/25600) | (y > -sqrt(4252855)/1024)) & ((y > 3*sqrt(295264335)/25600) | (y < -3*sqrt(295264335)/25600)) & ((y > -sqrt(4252855)/1024) | (y < sqrt(4252855)/1024)) & ((y < -3*sqrt(295264335)/25600) | (y < sqrt(4252855)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(295264335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4252855), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(295264335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(295264335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4252855), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4252855), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(295264335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4252855), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(y:sympy.Rational):
	#((y > sqrt(10981672935)/51200) | (y > -sqrt(17574871)/2048)) & ((y > sqrt(10981672935)/51200) | (y < -sqrt(10981672935)/51200)) & ((y > -sqrt(17574871)/2048) | (y < sqrt(17574871)/2048)) & ((y < -sqrt(10981672935)/51200) | (y < sqrt(17574871)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10981672935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17574871), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10981672935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10981672935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17574871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17574871), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10981672935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17574871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(y:sympy.Rational):
	#((y > sqrt(10897927935)/51200) | (y > -sqrt(17440879)/2048)) & ((y > sqrt(10897927935)/51200) | (y < -sqrt(10897927935)/51200)) & ((y > -sqrt(17440879)/2048) | (y < sqrt(17440879)/2048)) & ((y < -sqrt(10897927935)/51200) | (y < sqrt(17440879)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10897927935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17440879), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10897927935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10897927935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17440879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17440879), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10897927935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17440879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(y:sympy.Rational):
	#((y > sqrt(2766514015)/25600) | (y > -sqrt(4427471)/1024)) & ((y > sqrt(2766514015)/25600) | (y < -sqrt(2766514015)/25600)) & ((y > -sqrt(4427471)/1024) | (y < sqrt(4427471)/1024)) & ((y < -sqrt(2766514015)/25600) | (y < sqrt(4427471)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2766514015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4427471), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2766514015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2766514015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4427471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4427471), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2766514015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4427471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(y:sympy.Rational):
	#((y > sqrt(10577002935)/51200) | (y > -sqrt(16927399)/2048)) & ((y > sqrt(10577002935)/51200) | (y < -sqrt(10577002935)/51200)) & ((y > -sqrt(16927399)/2048) | (y < sqrt(16927399)/2048)) & ((y < -sqrt(10577002935)/51200) | (y < sqrt(16927399)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10577002935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16927399), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10577002935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10577002935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16927399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16927399), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10577002935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16927399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(y:sympy.Rational):
	#((y > sqrt(10571972935)/51200) | (y > -79*sqrt(2711)/2048)) & ((y > sqrt(10571972935)/51200) | (y < -sqrt(10571972935)/51200)) & ((y > -79*sqrt(2711)/2048) | (y < 79*sqrt(2711)/2048)) & ((y < -sqrt(10571972935)/51200) | (y < 79*sqrt(2711)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10571972935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(79, 2048), Pow(Integer(2711), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10571972935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10571972935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(79, 2048), Pow(Integer(2711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(79, 2048), Pow(Integer(2711), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10571972935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(79, 2048), Pow(Integer(2711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(y:sympy.Rational):
	#((y > sqrt(11108722935)/51200) | (y > -sqrt(17778151)/2048)) & ((y > sqrt(11108722935)/51200) | (y < -sqrt(11108722935)/51200)) & ((y > -sqrt(17778151)/2048) | (y < sqrt(17778151)/2048)) & ((y < -sqrt(11108722935)/51200) | (y < sqrt(17778151)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11108722935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17778151), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11108722935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11108722935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17778151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17778151), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11108722935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17778151), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(y:sympy.Rational):
	#((y > sqrt(2782194015)/25600) | (y > -sqrt(4452559)/1024)) & ((y > sqrt(2782194015)/25600) | (y < -sqrt(2782194015)/25600)) & ((y > -sqrt(4452559)/1024) | (y < sqrt(4452559)/1024)) & ((y < -sqrt(2782194015)/25600) | (y < sqrt(4452559)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2782194015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4452559), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2782194015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2782194015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4452559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4452559), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2782194015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4452559), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(y:sympy.Rational):
	#((y > sqrt(11022937935)/51200) | (y > -sqrt(17640895)/2048)) & ((y > sqrt(11022937935)/51200) | (y < -sqrt(11022937935)/51200)) & ((y > -sqrt(17640895)/2048) | (y < sqrt(17640895)/2048)) & ((y < -sqrt(11022937935)/51200) | (y < sqrt(17640895)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11022937935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17640895), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11022937935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11022937935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17640895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17640895), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11022937935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17640895), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(y:sympy.Rational):
	#((y > sqrt(10855447935)/51200) | (y > -sqrt(17372911)/2048)) & ((y > sqrt(10855447935)/51200) | (y < -sqrt(10855447935)/51200)) & ((y > -sqrt(17372911)/2048) | (y < sqrt(17372911)/2048)) & ((y < -sqrt(10855447935)/51200) | (y < sqrt(17372911)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10855447935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17372911), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10855447935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10855447935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17372911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17372911), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10855447935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17372911), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(y:sympy.Rational):
	#((y > -sqrt(16813999)/2048) | (y > 59*sqrt(3018135)/51200)) & ((y > -sqrt(16813999)/2048) | (y < sqrt(16813999)/2048)) & ((y > 59*sqrt(3018135)/51200) | (y < -59*sqrt(3018135)/51200)) & ((y < sqrt(16813999)/2048) | (y < -59*sqrt(3018135)/51200))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16813999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(59, 51200), Pow(Integer(3018135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16813999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16813999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(59, 51200), Pow(Integer(3018135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(59, 51200), Pow(Integer(3018135), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16813999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(59, 51200), Pow(Integer(3018135), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(y:sympy.Rational):
	#((y > sqrt(11139872935)/51200) | (y > -sqrt(17827991)/2048)) & ((y > sqrt(11139872935)/51200) | (y < -sqrt(11139872935)/51200)) & ((y > -sqrt(17827991)/2048) | (y < sqrt(17827991)/2048)) & ((y < -sqrt(11139872935)/51200) | (y < sqrt(17827991)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11139872935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17827991), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11139872935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11139872935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17827991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17827991), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11139872935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17827991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(y:sympy.Rational):
	#((y > -sqrt(1057711)/512) | (y > sqrt(660905535)/12800)) & ((y > -sqrt(1057711)/512) | (y < sqrt(1057711)/512)) & ((y > sqrt(660905535)/12800) | (y < -sqrt(660905535)/12800)) & ((y < sqrt(1057711)/512) | (y < -sqrt(660905535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1057711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(660905535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1057711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1057711), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(660905535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(660905535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1057711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(660905535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(y:sympy.Rational):
	#((y > sqrt(10836437935)/51200) | (y > -sqrt(17342495)/2048)) & ((y > sqrt(10836437935)/51200) | (y < -sqrt(10836437935)/51200)) & ((y > -sqrt(17342495)/2048) | (y < sqrt(17342495)/2048)) & ((y < -sqrt(10836437935)/51200) | (y < sqrt(17342495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10836437935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17342495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10836437935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10836437935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17342495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17342495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10836437935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17342495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(y:sympy.Rational):
	#((y > -sqrt(1114471)/512) | (y > 3*sqrt(77375615)/12800)) & ((y > -sqrt(1114471)/512) | (y < sqrt(1114471)/512)) & ((y > 3*sqrt(77375615)/12800) | (y < -3*sqrt(77375615)/12800)) & ((y < sqrt(1114471)/512) | (y < -3*sqrt(77375615)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1114471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(77375615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1114471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1114471), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(77375615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(77375615), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1114471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(77375615), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(y:sympy.Rational):
	#((y > sqrt(10621815)/1600) | (y > -sqrt(16999)/64)) & ((y > sqrt(10621815)/1600) | (y < -sqrt(10621815)/1600)) & ((y > -sqrt(16999)/64) | (y < sqrt(16999)/64)) & ((y < -sqrt(10621815)/1600) | (y < sqrt(16999)/64))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(10621815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(10621815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(10621815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16999), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(10621815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(y:sympy.Rational):
	#((y > sqrt(10597072935)/51200) | (y > -sqrt(16959511)/2048)) & ((y > sqrt(10597072935)/51200) | (y < -sqrt(10597072935)/51200)) & ((y > -sqrt(16959511)/2048) | (y < sqrt(16959511)/2048)) & ((y < -sqrt(10597072935)/51200) | (y < sqrt(16959511)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10597072935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16959511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10597072935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10597072935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16959511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16959511), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10597072935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16959511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(y:sympy.Rational):
	#((y > sqrt(10888522935)/51200) | (y > -19*sqrt(48271)/2048)) & ((y > sqrt(10888522935)/51200) | (y < -sqrt(10888522935)/51200)) & ((y > -19*sqrt(48271)/2048) | (y < 19*sqrt(48271)/2048)) & ((y < -sqrt(10888522935)/51200) | (y < 19*sqrt(48271)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10888522935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(19, 2048), Pow(Integer(48271), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10888522935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10888522935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(19, 2048), Pow(Integer(48271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(19, 2048), Pow(Integer(48271), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10888522935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(19, 2048), Pow(Integer(48271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(y:sympy.Rational):
	#((y > sqrt(10940002935)/51200) | (y > -sqrt(17508199)/2048)) & ((y > sqrt(10940002935)/51200) | (y < -sqrt(10940002935)/51200)) & ((y > -sqrt(17508199)/2048) | (y < sqrt(17508199)/2048)) & ((y < -sqrt(10940002935)/51200) | (y < sqrt(17508199)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10940002935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17508199), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10940002935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10940002935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17508199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17508199), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10940002935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17508199), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(y:sympy.Rational):
	#((y > sqrt(2642364015)/25600) | (y > -sqrt(4228831)/1024)) & ((y > sqrt(2642364015)/25600) | (y < -sqrt(2642364015)/25600)) & ((y > -sqrt(4228831)/1024) | (y < sqrt(4228831)/1024)) & ((y < -sqrt(2642364015)/25600) | (y < sqrt(4228831)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2642364015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4228831), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2642364015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2642364015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4228831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4228831), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2642364015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4228831), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(y:sympy.Rational):
	#((y > sqrt(2706129015)/25600) | (y > -sqrt(4330855)/1024)) & ((y > sqrt(2706129015)/25600) | (y < -sqrt(2706129015)/25600)) & ((y > -sqrt(4330855)/1024) | (y < sqrt(4330855)/1024)) & ((y < -sqrt(2706129015)/25600) | (y < sqrt(4330855)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2706129015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4330855), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2706129015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2706129015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4330855), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4330855), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2706129015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4330855), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(y:sympy.Rational):
	#((y > -59*sqrt(1255)/1024) | (y > sqrt(2729754015)/25600)) & ((y > -59*sqrt(1255)/1024) | (y < 59*sqrt(1255)/1024)) & ((y > sqrt(2729754015)/25600) | (y < -sqrt(2729754015)/25600)) & ((y < 59*sqrt(1255)/1024) | (y < -sqrt(2729754015)/25600))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(59, 1024), Pow(Integer(1255), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2729754015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(59, 1024), Pow(Integer(1255), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(59, 1024), Pow(Integer(1255), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2729754015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2729754015), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(59, 1024), Pow(Integer(1255), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2729754015), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(y:sympy.Rational):
	#((y > sqrt(43489135)/3200) | (y > -sqrt(69599)/128)) & ((y > sqrt(43489135)/3200) | (y < -sqrt(43489135)/3200)) & ((y > -sqrt(69599)/128) | (y < sqrt(69599)/128)) & ((y < -sqrt(43489135)/3200) | (y < sqrt(69599)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(43489135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(43489135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(43489135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69599), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(43489135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(y:sympy.Rational):
	#((y > 3*sqrt(3819215)/51200) | (y > -sqrt(59191)/2048)) & ((y > 3*sqrt(3819215)/51200) | (y < -3*sqrt(3819215)/51200)) & ((y > -sqrt(59191)/2048) | (y < sqrt(59191)/2048)) & ((y < -3*sqrt(3819215)/51200) | (y < sqrt(59191)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(3819215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(59191), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(3819215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(3819215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(59191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(59191), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(3819215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(59191), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(y:sympy.Rational):
	#((y > -sqrt(1086991)/512) | (y > sqrt(679205535)/12800)) & ((y > -sqrt(1086991)/512) | (y < sqrt(1086991)/512)) & ((y > sqrt(679205535)/12800) | (y < -sqrt(679205535)/12800)) & ((y < sqrt(1086991)/512) | (y < -sqrt(679205535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1086991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(679205535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1086991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1086991), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(679205535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(679205535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1086991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(679205535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(y:sympy.Rational):
	#((y > sqrt(2718004015)/25600) | (y > -sqrt(4349855)/1024)) & ((y > sqrt(2718004015)/25600) | (y < -sqrt(2718004015)/25600)) & ((y > -sqrt(4349855)/1024) | (y < sqrt(4349855)/1024)) & ((y < -sqrt(2718004015)/25600) | (y < sqrt(4349855)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2718004015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4349855), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2718004015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2718004015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4349855), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4349855), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2718004015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4349855), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(y:sympy.Rational):
	#((y > sqrt(11144302935)/51200) | (y > -sqrt(17835079)/2048)) & ((y > sqrt(11144302935)/51200) | (y < -sqrt(11144302935)/51200)) & ((y > -sqrt(17835079)/2048) | (y < sqrt(17835079)/2048)) & ((y < -sqrt(11144302935)/51200) | (y < sqrt(17835079)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11144302935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17835079), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11144302935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11144302935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17835079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17835079), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11144302935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17835079), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(y:sympy.Rational):
	#((y > sqrt(10582027935)/51200) | (y > -sqrt(16935439)/2048)) & ((y > sqrt(10582027935)/51200) | (y < -sqrt(10582027935)/51200)) & ((y > -sqrt(16935439)/2048) | (y < sqrt(16935439)/2048)) & ((y < -sqrt(10582027935)/51200) | (y < sqrt(16935439)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10582027935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16935439), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10582027935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10582027935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16935439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16935439), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10582027935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16935439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(y:sympy.Rational):
	#((y > sqrt(10495922935)/51200) | (y > -sqrt(16797671)/2048)) & ((y > sqrt(10495922935)/51200) | (y < -sqrt(10495922935)/51200)) & ((y > -sqrt(16797671)/2048) | (y < sqrt(16797671)/2048)) & ((y < -sqrt(10495922935)/51200) | (y < sqrt(16797671)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10495922935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16797671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10495922935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10495922935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16797671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16797671), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10495922935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16797671), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(y:sympy.Rational):
	#((y > 3*sqrt(1235294215)/51200) | (y > -sqrt(17792431)/2048)) & ((y > 3*sqrt(1235294215)/51200) | (y < -3*sqrt(1235294215)/51200)) & ((y > -sqrt(17792431)/2048) | (y < sqrt(17792431)/2048)) & ((y < -3*sqrt(1235294215)/51200) | (y < sqrt(17792431)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1235294215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17792431), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1235294215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1235294215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17792431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17792431), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1235294215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17792431), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(y:sympy.Rational):
	#((y > sqrt(2727414015)/25600) | (y > -sqrt(4364911)/1024)) & ((y > sqrt(2727414015)/25600) | (y < -sqrt(2727414015)/25600)) & ((y > -sqrt(4364911)/1024) | (y < sqrt(4364911)/1024)) & ((y < -sqrt(2727414015)/25600) | (y < sqrt(4364911)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2727414015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4364911), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2727414015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2727414015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4364911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4364911), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2727414015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4364911), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(y:sympy.Rational):
	#((y > sqrt(2750589015)/25600) | (y > -sqrt(4401991)/1024)) & ((y > sqrt(2750589015)/25600) | (y < -sqrt(2750589015)/25600)) & ((y > -sqrt(4401991)/1024) | (y < sqrt(4401991)/1024)) & ((y < -sqrt(2750589015)/25600) | (y < sqrt(4401991)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2750589015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4401991), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2750589015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2750589015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4401991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4401991), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2750589015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4401991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(y:sympy.Rational):
	#((y > 3*sqrt(18375935)/6400) | (y > -sqrt(264679)/256)) & ((y > 3*sqrt(18375935)/6400) | (y < -3*sqrt(18375935)/6400)) & ((y > -sqrt(264679)/256) | (y < sqrt(264679)/256)) & ((y < -3*sqrt(18375935)/6400) | (y < sqrt(264679)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18375935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(264679), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18375935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18375935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(264679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(264679), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18375935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(264679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(y:sympy.Rational):
	#((y > sqrt(10501027935)/51200) | (y > -sqrt(16805839)/2048)) & ((y > sqrt(10501027935)/51200) | (y < -sqrt(10501027935)/51200)) & ((y > -sqrt(16805839)/2048) | (y < sqrt(16805839)/2048)) & ((y < -sqrt(10501027935)/51200) | (y < sqrt(16805839)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10501027935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16805839), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10501027935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10501027935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16805839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16805839), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10501027935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16805839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(y:sympy.Rational):
	#((y > sqrt(148923615)/102400) | (y > -sqrt(255055)/4096)) & ((y > sqrt(148923615)/102400) | (y < -sqrt(148923615)/102400)) & ((y > -sqrt(255055)/4096) | (y < sqrt(255055)/4096)) & ((y < -sqrt(148923615)/102400) | (y < sqrt(255055)/4096))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(148923615), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(255055), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(148923615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(148923615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(255055), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(255055), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(148923615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(255055), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(y:sympy.Rational):
	#((y > 3*sqrt(309379335)/25600) | (y > -sqrt(4456111)/1024)) & ((y > 3*sqrt(309379335)/25600) | (y < -3*sqrt(309379335)/25600)) & ((y > -sqrt(4456111)/1024) | (y < sqrt(4456111)/1024)) & ((y < -3*sqrt(309379335)/25600) | (y < sqrt(4456111)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(309379335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4456111), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(309379335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(309379335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4456111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4456111), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(309379335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4456111), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(y:sympy.Rational):
	#((y > sqrt(2748294015)/25600) | (y > -sqrt(4398319)/1024)) & ((y > sqrt(2748294015)/25600) | (y < -sqrt(2748294015)/25600)) & ((y > -sqrt(4398319)/1024) | (y < sqrt(4398319)/1024)) & ((y < -sqrt(2748294015)/25600) | (y < sqrt(4398319)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2748294015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4398319), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2748294015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2748294015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4398319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4398319), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2748294015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4398319), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(y:sympy.Rational):
	#((y > sqrt(164118415)/6400) | (y > -sqrt(262655)/256)) & ((y > sqrt(164118415)/6400) | (y < -sqrt(164118415)/6400)) & ((y > -sqrt(262655)/256) | (y < sqrt(262655)/256)) & ((y < -sqrt(164118415)/6400) | (y < sqrt(262655)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(164118415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(262655), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(164118415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(164118415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(262655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(262655), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(164118415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(262655), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(y:sympy.Rational):
	#((y > sqrt(2732089015)/25600) | (y > -sqrt(4372391)/1024)) & ((y > sqrt(2732089015)/25600) | (y < -sqrt(2732089015)/25600)) & ((y > -sqrt(4372391)/1024) | (y < sqrt(4372391)/1024)) & ((y < -sqrt(2732089015)/25600) | (y < sqrt(4372391)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2732089015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4372391), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2732089015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2732089015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4372391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4372391), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2732089015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4372391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(y:sympy.Rational):
	#((y > -sqrt(1056799)/8192) | (y > sqrt(618556335)/204800)) & ((y > -sqrt(1056799)/8192) | (y < sqrt(1056799)/8192)) & ((y > sqrt(618556335)/204800) | (y < -sqrt(618556335)/204800)) & ((y < sqrt(1056799)/8192) | (y < -sqrt(618556335)/204800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(1056799), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(618556335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(1056799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(1056799), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(618556335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(618556335), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(1056799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(618556335), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(y:sympy.Rational):
	#((y > sqrt(572831335)/204800) | (y > -sqrt(983639)/8192)) & ((y > sqrt(572831335)/204800) | (y < -sqrt(572831335)/204800)) & ((y > -sqrt(983639)/8192) | (y < sqrt(983639)/8192)) & ((y < -sqrt(572831335)/204800) | (y < sqrt(983639)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(572831335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(983639), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(572831335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(572831335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(983639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(983639), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(572831335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(983639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(y:sympy.Rational):
	#((y > sqrt(172553415)/6400) | (y > -sqrt(276151)/256)) & ((y > sqrt(172553415)/6400) | (y < -sqrt(172553415)/6400)) & ((y > -sqrt(276151)/256) | (y < sqrt(276151)/256)) & ((y < -sqrt(172553415)/6400) | (y < sqrt(276151)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(172553415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(276151), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(172553415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(172553415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(276151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(276151), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(172553415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(276151), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(y:sympy.Rational):
	#((y > sqrt(126058615)/102400) | (y > -sqrt(218471)/4096)) & ((y > sqrt(126058615)/102400) | (y < -sqrt(126058615)/102400)) & ((y > -sqrt(218471)/4096) | (y < sqrt(218471)/4096)) & ((y < -sqrt(126058615)/102400) | (y < sqrt(218471)/4096))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(126058615), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(218471), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(126058615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(126058615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(218471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(218471), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(126058615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(218471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(y:sympy.Rational):
	#((y > -sqrt(1096351)/512) | (y > sqrt(685055535)/12800)) & ((y > -sqrt(1096351)/512) | (y < sqrt(1096351)/512)) & ((y > sqrt(685055535)/12800) | (y < -sqrt(685055535)/12800)) & ((y < sqrt(1096351)/512) | (y < -sqrt(685055535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1096351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(685055535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1096351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1096351), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(685055535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(685055535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1096351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(685055535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(y:sympy.Rational):
	#((y > sqrt(11135437935)/51200) | (y > -sqrt(17820895)/2048)) & ((y > sqrt(11135437935)/51200) | (y < -sqrt(11135437935)/51200)) & ((y > -sqrt(17820895)/2048) | (y < sqrt(17820895)/2048)) & ((y < -sqrt(11135437935)/51200) | (y < sqrt(17820895)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11135437935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17820895), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11135437935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11135437935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17820895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17820895), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11135437935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17820895), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(y:sympy.Rational):
	#((y > sqrt(11130997935)/51200) | (y > -sqrt(17813791)/2048)) & ((y > sqrt(11130997935)/51200) | (y < -sqrt(11130997935)/51200)) & ((y > -sqrt(17813791)/2048) | (y < sqrt(17813791)/2048)) & ((y < -sqrt(11130997935)/51200) | (y < sqrt(17813791)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11130997935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17813791), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11130997935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11130997935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17813791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17813791), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11130997935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17813791), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(y:sympy.Rational):
	#((y > sqrt(10935347935)/51200) | (y > -sqrt(17500751)/2048)) & ((y > sqrt(10935347935)/51200) | (y < -sqrt(10935347935)/51200)) & ((y > -sqrt(17500751)/2048) | (y < sqrt(17500751)/2048)) & ((y < -sqrt(10935347935)/51200) | (y < sqrt(17500751)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10935347935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17500751), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10935347935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10935347935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17500751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17500751), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10935347935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17500751), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(y:sympy.Rational):
	#((y > sqrt(10592062935)/51200) | (y > -11*sqrt(140095)/2048)) & ((y > sqrt(10592062935)/51200) | (y < -sqrt(10592062935)/51200)) & ((y > -11*sqrt(140095)/2048) | (y < 11*sqrt(140095)/2048)) & ((y < -sqrt(10592062935)/51200) | (y < 11*sqrt(140095)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10592062935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 2048), Pow(Integer(140095), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10592062935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10592062935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 2048), Pow(Integer(140095), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 2048), Pow(Integer(140095), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10592062935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 2048), Pow(Integer(140095), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(y:sympy.Rational):
	#((y > sqrt(2673735)/800) | (y > -sqrt(4279)/32)) & ((y > sqrt(2673735)/800) | (y < -sqrt(2673735)/800)) & ((y > -sqrt(4279)/32) | (y < sqrt(4279)/32)) & ((y < -sqrt(2673735)/800) | (y < sqrt(4279)/32))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 800), Pow(Integer(2673735), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4279), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 800), Pow(Integer(2673735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 800), Pow(Integer(2673735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4279), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 800), Pow(Integer(2673735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(y:sympy.Rational):
	#((y > -sqrt(1103695)/512) | (y > sqrt(689645535)/12800)) & ((y > -sqrt(1103695)/512) | (y < sqrt(1103695)/512)) & ((y > sqrt(689645535)/12800) | (y < -sqrt(689645535)/12800)) & ((y < sqrt(1103695)/512) | (y < -sqrt(689645535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1103695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(689645535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1103695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1103695), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(689645535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(689645535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1103695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(689645535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(y:sympy.Rational):
	#((y > sqrt(10556852935)/51200) | (y > -sqrt(16895159)/2048)) & ((y > sqrt(10556852935)/51200) | (y < -sqrt(10556852935)/51200)) & ((y > -sqrt(16895159)/2048) | (y < sqrt(16895159)/2048)) & ((y < -sqrt(10556852935)/51200) | (y < sqrt(16895159)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10556852935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16895159), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10556852935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10556852935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16895159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16895159), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10556852935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16895159), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(y:sympy.Rational):
	#((y > sqrt(2757444015)/25600) | (y > -sqrt(4412959)/1024)) & ((y > sqrt(2757444015)/25600) | (y < -sqrt(2757444015)/25600)) & ((y > -sqrt(4412959)/1024) | (y < sqrt(4412959)/1024)) & ((y < -sqrt(2757444015)/25600) | (y < sqrt(4412959)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2757444015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4412959), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2757444015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2757444015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4412959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4412959), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2757444015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4412959), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(y:sympy.Rational):
	#((y > sqrt(10536622935)/51200) | (y > -sqrt(16862791)/2048)) & ((y > sqrt(10536622935)/51200) | (y < -sqrt(10536622935)/51200)) & ((y > -sqrt(16862791)/2048) | (y < sqrt(16862791)/2048)) & ((y < -sqrt(10536622935)/51200) | (y < sqrt(16862791)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10536622935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16862791), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10536622935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10536622935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16862791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16862791), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10536622935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16862791), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(y:sympy.Rational):
	#((y > sqrt(11086322935)/51200) | (y > -sqrt(17742311)/2048)) & ((y > sqrt(11086322935)/51200) | (y < -sqrt(11086322935)/51200)) & ((y > -sqrt(17742311)/2048) | (y < sqrt(17742311)/2048)) & ((y < -sqrt(11086322935)/51200) | (y < sqrt(17742311)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11086322935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17742311), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11086322935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11086322935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17742311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17742311), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11086322935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17742311), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(y:sympy.Rational):
	#((y > 3*sqrt(58566815)/204800) | (y > -sqrt(910471)/8192)) & ((y > 3*sqrt(58566815)/204800) | (y < -3*sqrt(58566815)/204800)) & ((y > -sqrt(910471)/8192) | (y < sqrt(910471)/8192)) & ((y < -3*sqrt(58566815)/204800) | (y < sqrt(910471)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 204800), Pow(Integer(58566815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(910471), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 204800), Pow(Integer(58566815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 204800), Pow(Integer(58566815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(910471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(910471), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 204800), Pow(Integer(58566815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(910471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(y:sympy.Rational):
	#((y > sqrt(2644879015)/25600) | (y > -sqrt(4232855)/1024)) & ((y > sqrt(2644879015)/25600) | (y < -sqrt(2644879015)/25600)) & ((y > -sqrt(4232855)/1024) | (y < sqrt(4232855)/1024)) & ((y < -sqrt(2644879015)/25600) | (y < sqrt(4232855)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2644879015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4232855), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2644879015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2644879015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4232855), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4232855), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2644879015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4232855), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(y:sympy.Rational):
	#((y > sqrt(10602077935)/51200) | (y > -sqrt(16967519)/2048)) & ((y > sqrt(10602077935)/51200) | (y < -sqrt(10602077935)/51200)) & ((y > -sqrt(16967519)/2048) | (y < sqrt(16967519)/2048)) & ((y < -sqrt(10602077935)/51200) | (y < sqrt(16967519)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10602077935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16967519), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10602077935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10602077935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16967519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16967519), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10602077935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16967519), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(y:sympy.Rational):
	#((y > 3*sqrt(303824335)/25600) | (y > -sqrt(4376119)/1024)) & ((y > 3*sqrt(303824335)/25600) | (y < -3*sqrt(303824335)/25600)) & ((y > -sqrt(4376119)/1024) | (y < sqrt(4376119)/1024)) & ((y < -3*sqrt(303824335)/25600) | (y < sqrt(4376119)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(303824335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4376119), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(303824335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(303824335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4376119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4376119), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(303824335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4376119), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(y:sympy.Rational):
	#((y > -sqrt(1100039)/512) | (y > sqrt(687360535)/12800)) & ((y > -sqrt(1100039)/512) | (y < sqrt(1100039)/512)) & ((y > sqrt(687360535)/12800) | (y < -sqrt(687360535)/12800)) & ((y < sqrt(1100039)/512) | (y < -sqrt(687360535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1100039), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(687360535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1100039), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1100039), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(687360535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(687360535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1100039), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(687360535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(y:sympy.Rational):
	#((y > sqrt(2715639015)/25600) | (y > -sqrt(4346071)/1024)) & ((y > sqrt(2715639015)/25600) | (y < -sqrt(2715639015)/25600)) & ((y > -sqrt(4346071)/1024) | (y < sqrt(4346071)/1024)) & ((y < -sqrt(2715639015)/25600) | (y < sqrt(4346071)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2715639015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4346071), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2715639015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2715639015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4346071), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4346071), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2715639015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4346071), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(y:sympy.Rational):
	#((y > sqrt(2739064015)/25600) | (y > -sqrt(4383551)/1024)) & ((y > sqrt(2739064015)/25600) | (y < -sqrt(2739064015)/25600)) & ((y > -sqrt(4383551)/1024) | (y < sqrt(4383551)/1024)) & ((y < -sqrt(2739064015)/25600) | (y < sqrt(4383551)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2739064015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4383551), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2739064015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2739064015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4383551), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4383551), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2739064015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4383551), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(y:sympy.Rational):
	#((y > sqrt(2759719015)/25600) | (y > -sqrt(4416599)/1024)) & ((y > sqrt(2759719015)/25600) | (y < -sqrt(2759719015)/25600)) & ((y > -sqrt(4416599)/1024) | (y < sqrt(4416599)/1024)) & ((y < -sqrt(2759719015)/25600) | (y < sqrt(4416599)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2759719015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4416599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2759719015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2759719015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4416599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4416599), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2759719015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4416599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(y:sympy.Rational):
	#((y > 27*sqrt(3631535)/25600) | (y > -sqrt(4236871)/1024)) & ((y > 27*sqrt(3631535)/25600) | (y < -27*sqrt(3631535)/25600)) & ((y > -sqrt(4236871)/1024) | (y < sqrt(4236871)/1024)) & ((y < -27*sqrt(3631535)/25600) | (y < sqrt(4236871)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(27, 25600), Pow(Integer(3631535), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4236871), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(27, 25600), Pow(Integer(3631535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(27, 25600), Pow(Integer(3631535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4236871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4236871), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(27, 25600), Pow(Integer(3631535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4236871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(y:sympy.Rational):
	#((y > 3*sqrt(1207739215)/51200) | (y > -sqrt(17395639)/2048)) & ((y > 3*sqrt(1207739215)/51200) | (y < -3*sqrt(1207739215)/51200)) & ((y > -sqrt(17395639)/2048) | (y < sqrt(17395639)/2048)) & ((y < -3*sqrt(1207739215)/51200) | (y < sqrt(17395639)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1207739215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17395639), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1207739215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1207739215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17395639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17395639), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1207739215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17395639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(y:sympy.Rational):
	#((y > sqrt(41424135)/3200) | (y > -sqrt(66295)/128)) & ((y > sqrt(41424135)/3200) | (y < -sqrt(41424135)/3200)) & ((y > -sqrt(66295)/128) | (y < sqrt(66295)/128)) & ((y < -sqrt(41424135)/3200) | (y < sqrt(66295)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(41424135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(66295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(41424135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(41424135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(66295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(66295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(41424135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(66295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(y:sympy.Rational):
	#((y > -sqrt(181879)/4096) | (y > 53*sqrt(36735)/102400)) & ((y > -sqrt(181879)/4096) | (y < sqrt(181879)/4096)) & ((y > 53*sqrt(36735)/102400) | (y < -53*sqrt(36735)/102400)) & ((y < sqrt(181879)/4096) | (y < -53*sqrt(36735)/102400))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(181879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(53, 102400), Pow(Integer(36735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(181879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(181879), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(53, 102400), Pow(Integer(36735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(53, 102400), Pow(Integer(36735), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(181879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(53, 102400), Pow(Integer(36735), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(y:sympy.Rational):
	#((y > sqrt(10944652935)/51200) | (y > -sqrt(17515639)/2048)) & ((y > sqrt(10944652935)/51200) | (y < -sqrt(10944652935)/51200)) & ((y > -sqrt(17515639)/2048) | (y < sqrt(17515639)/2048)) & ((y < -sqrt(10944652935)/51200) | (y < sqrt(17515639)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10944652935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17515639), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10944652935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10944652935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17515639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17515639), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10944652935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17515639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(y:sympy.Rational):
	#((y > sqrt(389881335)/204800) | (y > -sqrt(690919)/8192)) & ((y > sqrt(389881335)/204800) | (y < -sqrt(389881335)/204800)) & ((y > -sqrt(690919)/8192) | (y < sqrt(690919)/8192)) & ((y < -sqrt(389881335)/204800) | (y < sqrt(690919)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(389881335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(690919), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(389881335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(389881335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(690919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(690919), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(389881335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(690919), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(y:sympy.Rational):
	#((y > sqrt(10490812935)/51200) | (y > -sqrt(16789495)/2048)) & ((y > sqrt(10490812935)/51200) | (y < -sqrt(10490812935)/51200)) & ((y > -sqrt(16789495)/2048) | (y < sqrt(16789495)/2048)) & ((y < -sqrt(10490812935)/51200) | (y < sqrt(16789495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10490812935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16789495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10490812935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10490812935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16789495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16789495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10490812935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16789495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(y:sympy.Rational):
	#((y > 3*sqrt(18815)/200) | (y > -sqrt(271)/8)) & ((y > 3*sqrt(18815)/200) | (y < -3*sqrt(18815)/200)) & ((y > -sqrt(271)/8) | (y < sqrt(271)/8)) & ((y < -3*sqrt(18815)/200) | (y < sqrt(271)/8))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 200), Pow(Integer(18815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(271), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 200), Pow(Integer(18815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 200), Pow(Integer(18815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(271), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 200), Pow(Integer(18815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(y:sympy.Rational):
	#((y > sqrt(10551802935)/51200) | (y > -sqrt(16887079)/2048)) & ((y > sqrt(10551802935)/51200) | (y < -sqrt(10551802935)/51200)) & ((y > -sqrt(16887079)/2048) | (y < sqrt(16887079)/2048)) & ((y < -sqrt(10551802935)/51200) | (y < sqrt(16887079)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10551802935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16887079), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10551802935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10551802935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16887079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16887079), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10551802935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16887079), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(y:sympy.Rational):
	#((y > -sqrt(12511)/1024) | (y > sqrt(7164015)/25600)) & ((y > -sqrt(12511)/1024) | (y < sqrt(12511)/1024)) & ((y > sqrt(7164015)/25600) | (y < -sqrt(7164015)/25600)) & ((y < sqrt(12511)/1024) | (y < -sqrt(7164015)/25600))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(12511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(7164015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(12511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(12511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(7164015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(7164015), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(12511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(7164015), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(y:sympy.Rational):
	#((y > sqrt(11013802935)/51200) | (y > -sqrt(17626279)/2048)) & ((y > sqrt(11013802935)/51200) | (y < -sqrt(11013802935)/51200)) & ((y > -sqrt(17626279)/2048) | (y < sqrt(17626279)/2048)) & ((y < -sqrt(11013802935)/51200) | (y < sqrt(17626279)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11013802935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17626279), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11013802935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11013802935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17626279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17626279), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11013802935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17626279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(y:sympy.Rational):
	#((y > -sqrt(1049599)/512) | (y > 9*sqrt(8096735)/12800)) & ((y > -sqrt(1049599)/512) | (y < sqrt(1049599)/512)) & ((y > 9*sqrt(8096735)/12800) | (y < -9*sqrt(8096735)/12800)) & ((y < sqrt(1049599)/512) | (y < -9*sqrt(8096735)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1049599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(9, 12800), Pow(Integer(8096735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1049599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1049599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 12800), Pow(Integer(8096735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 12800), Pow(Integer(8096735), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1049599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 12800), Pow(Integer(8096735), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(y:sympy.Rational):
	#((y > sqrt(435626335)/204800) | (y > -sqrt(764111)/8192)) & ((y > sqrt(435626335)/204800) | (y < -sqrt(435626335)/204800)) & ((y > -sqrt(764111)/8192) | (y < sqrt(764111)/8192)) & ((y < -sqrt(435626335)/204800) | (y < sqrt(764111)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(435626335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(764111), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(435626335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(435626335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(764111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(764111), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(435626335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(764111), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(y:sympy.Rational):
	#((y > sqrt(2659864015)/25600) | (y > -sqrt(4256831)/1024)) & ((y > sqrt(2659864015)/25600) | (y < -sqrt(2659864015)/25600)) & ((y > -sqrt(4256831)/1024) | (y < sqrt(4256831)/1024)) & ((y < -sqrt(2659864015)/25600) | (y < sqrt(4256831)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2659864015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4256831), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2659864015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2659864015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4256831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4256831), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2659864015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4256831), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(y:sympy.Rational):
	#((y > 3*sqrt(1168479215)/51200) | (y > -sqrt(16830295)/2048)) & ((y > 3*sqrt(1168479215)/51200) | (y < -3*sqrt(1168479215)/51200)) & ((y > -sqrt(16830295)/2048) | (y < sqrt(16830295)/2048)) & ((y < -3*sqrt(1168479215)/51200) | (y < sqrt(16830295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1168479215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16830295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1168479215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1168479215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16830295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16830295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1168479215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16830295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(y:sympy.Rational):
	#((y > sqrt(2598735)/800) | (y > -sqrt(4159)/32)) & ((y > sqrt(2598735)/800) | (y < -sqrt(2598735)/800)) & ((y > -sqrt(4159)/32) | (y < sqrt(4159)/32)) & ((y < -sqrt(2598735)/800) | (y < sqrt(4159)/32))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 800), Pow(Integer(2598735), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4159), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 800), Pow(Integer(2598735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 800), Pow(Integer(2598735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4159), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 800), Pow(Integer(2598735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4159), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(y:sympy.Rational):
	#((y > sqrt(2736744015)/25600) | (y > -sqrt(4379839)/1024)) & ((y > sqrt(2736744015)/25600) | (y < -sqrt(2736744015)/25600)) & ((y > -sqrt(4379839)/1024) | (y < sqrt(4379839)/1024)) & ((y < -sqrt(2736744015)/25600) | (y < sqrt(4379839)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2736744015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4379839), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2736744015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2736744015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4379839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4379839), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2736744015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4379839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(y:sympy.Rational):
	#((y > sqrt(11113187935)/51200) | (y > -sqrt(17785295)/2048)) & ((y > sqrt(11113187935)/51200) | (y < -sqrt(11113187935)/51200)) & ((y > -sqrt(17785295)/2048) | (y < sqrt(17785295)/2048)) & ((y < -sqrt(11113187935)/51200) | (y < sqrt(17785295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11113187935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17785295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11113187935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11113187935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17785295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17785295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11113187935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17785295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(y:sympy.Rational):
	#((y > -sqrt(1094495)/512) | (y > sqrt(683895535)/12800)) & ((y > -sqrt(1094495)/512) | (y < sqrt(1094495)/512)) & ((y > sqrt(683895535)/12800) | (y < -sqrt(683895535)/12800)) & ((y < sqrt(1094495)/512) | (y < -sqrt(683895535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1094495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(683895535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1094495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1094495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(683895535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(683895535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1094495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(683895535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(y:sympy.Rational):
	#((y > 3*sqrt(1226794215)/51200) | (y > -sqrt(17670031)/2048)) & ((y > 3*sqrt(1226794215)/51200) | (y < -3*sqrt(1226794215)/51200)) & ((y > -sqrt(17670031)/2048) | (y < sqrt(17670031)/2048)) & ((y < -3*sqrt(1226794215)/51200) | (y < sqrt(17670031)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1226794215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17670031), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1226794215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1226794215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17670031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17670031), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1226794215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17670031), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(y:sympy.Rational):
	#((y > sqrt(173678415)/6400) | (y > -sqrt(277951)/256)) & ((y > sqrt(173678415)/6400) | (y < -sqrt(173678415)/6400)) & ((y > -sqrt(277951)/256) | (y < sqrt(277951)/256)) & ((y < -sqrt(173678415)/6400) | (y < sqrt(277951)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(173678415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277951), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(173678415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(173678415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277951), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(173678415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(y:sympy.Rational):
	#((y > sqrt(2777739015)/25600) | (y > -sqrt(4445431)/1024)) & ((y > sqrt(2777739015)/25600) | (y < -sqrt(2777739015)/25600)) & ((y > -sqrt(4445431)/1024) | (y < sqrt(4445431)/1024)) & ((y < -sqrt(2777739015)/25600) | (y < sqrt(4445431)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2777739015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4445431), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2777739015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2777739015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4445431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4445431), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2777739015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4445431), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(y:sympy.Rational):
	#((y > sqrt(2637319015)/25600) | (y > -sqrt(4220759)/1024)) & ((y > sqrt(2637319015)/25600) | (y < -sqrt(2637319015)/25600)) & ((y > -sqrt(4220759)/1024) | (y < sqrt(4220759)/1024)) & ((y < -sqrt(2637319015)/25600) | (y < sqrt(4220759)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2637319015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4220759), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2637319015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2637319015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4220759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4220759), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2637319015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4220759), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(y:sympy.Rational):
	#((y > -sqrt(1112695)/512) | (y > sqrt(695270535)/12800)) & ((y > -sqrt(1112695)/512) | (y < sqrt(1112695)/512)) & ((y > sqrt(695270535)/12800) | (y < -sqrt(695270535)/12800)) & ((y < sqrt(1112695)/512) | (y < -sqrt(695270535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1112695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(695270535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1112695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1112695), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(695270535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(695270535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1112695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(695270535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(y:sympy.Rational):
	#((y > sqrt(2773264015)/25600) | (y > -sqrt(4438271)/1024)) & ((y > sqrt(2773264015)/25600) | (y < -sqrt(2773264015)/25600)) & ((y > -sqrt(4438271)/1024) | (y < sqrt(4438271)/1024)) & ((y < -sqrt(2773264015)/25600) | (y < sqrt(4438271)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2773264015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4438271), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2773264015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2773264015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4438271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4438271), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2773264015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4438271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(y:sympy.Rational):
	#((y > sqrt(11018372935)/51200) | (y > -sqrt(17633591)/2048)) & ((y > sqrt(11018372935)/51200) | (y < -sqrt(11018372935)/51200)) & ((y > -sqrt(17633591)/2048) | (y < sqrt(17633591)/2048)) & ((y < -sqrt(11018372935)/51200) | (y < sqrt(17633591)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11018372935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17633591), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11018372935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11018372935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17633591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17633591), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11018372935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17633591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(y:sympy.Rational):
	#((y > sqrt(42634135)/3200) | (y > -31*sqrt(71)/128)) & ((y > sqrt(42634135)/3200) | (y < -sqrt(42634135)/3200)) & ((y > -31*sqrt(71)/128) | (y < 31*sqrt(71)/128)) & ((y < -sqrt(42634135)/3200) | (y < 31*sqrt(71)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(42634135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(31, 128), Pow(Integer(71), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(42634135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(42634135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(31, 128), Pow(Integer(71), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(31, 128), Pow(Integer(71), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(42634135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(31, 128), Pow(Integer(71), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(y:sympy.Rational):
	#((y > 3*sqrt(308389335)/25600) | (y > -sqrt(4441855)/1024)) & ((y > 3*sqrt(308389335)/25600) | (y < -3*sqrt(308389335)/25600)) & ((y > -sqrt(4441855)/1024) | (y < sqrt(4441855)/1024)) & ((y < -3*sqrt(308389335)/25600) | (y < sqrt(4441855)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(308389335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4441855), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(308389335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(308389335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4441855), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4441855), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(308389335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4441855), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(y:sympy.Rational):
	#((y > -sqrt(108671)/4096) | (y > sqrt(57433615)/102400)) & ((y > -sqrt(108671)/4096) | (y < sqrt(108671)/4096)) & ((y > sqrt(57433615)/102400) | (y < -sqrt(57433615)/102400)) & ((y < sqrt(108671)/4096) | (y < -sqrt(57433615)/102400))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(108671), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(57433615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(108671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(108671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(57433615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(57433615), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(108671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(57433615), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(y:sympy.Rational):
	#((y > sqrt(169653415)/6400) | (y > -sqrt(271511)/256)) & ((y > sqrt(169653415)/6400) | (y < -sqrt(169653415)/6400)) & ((y > -sqrt(271511)/256) | (y < sqrt(271511)/256)) & ((y < -sqrt(169653415)/6400) | (y < sqrt(271511)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(169653415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(271511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(169653415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(169653415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(271511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(271511), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(169653415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(271511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(y:sympy.Rational):
	#((y > 3*sqrt(1226289215)/51200) | (y > -sqrt(17662759)/2048)) & ((y > 3*sqrt(1226289215)/51200) | (y < -3*sqrt(1226289215)/51200)) & ((y > -sqrt(17662759)/2048) | (y < sqrt(17662759)/2048)) & ((y < -3*sqrt(1226289215)/51200) | (y < sqrt(17662759)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1226289215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17662759), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1226289215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1226289215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17662759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17662759), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1226289215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17662759), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(y:sympy.Rational):
	#((y > sqrt(2649894015)/25600) | (y > -sqrt(4240879)/1024)) & ((y > sqrt(2649894015)/25600) | (y < -sqrt(2649894015)/25600)) & ((y > -sqrt(4240879)/1024) | (y < sqrt(4240879)/1024)) & ((y < -sqrt(2649894015)/25600) | (y < sqrt(4240879)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2649894015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4240879), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2649894015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2649894015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4240879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4240879), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2649894015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4240879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(y:sympy.Rational):
	#((y > sqrt(11126552935)/51200) | (y > -sqrt(17806679)/2048)) & ((y > sqrt(11126552935)/51200) | (y < -sqrt(11126552935)/51200)) & ((y > -sqrt(17806679)/2048) | (y < sqrt(17806679)/2048)) & ((y < -sqrt(11126552935)/51200) | (y < sqrt(17806679)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11126552935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17806679), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11126552935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11126552935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17806679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17806679), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11126552935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17806679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(y:sympy.Rational):
	#((y > sqrt(2779969015)/25600) | (y > -sqrt(4448999)/1024)) & ((y > sqrt(2779969015)/25600) | (y < -sqrt(2779969015)/25600)) & ((y > -sqrt(4448999)/1024) | (y < sqrt(4448999)/1024)) & ((y < -sqrt(2779969015)/25600) | (y < sqrt(4448999)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2779969015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4448999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2779969015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2779969015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4448999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4448999), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2779969015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4448999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(y:sympy.Rational):
	#((y > sqrt(10641937935)/51200) | (y > -sqrt(17031295)/2048)) & ((y > sqrt(10641937935)/51200) | (y < -sqrt(10641937935)/51200)) & ((y > -sqrt(17031295)/2048) | (y < sqrt(17031295)/2048)) & ((y < -sqrt(10641937935)/51200) | (y < sqrt(17031295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10641937935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17031295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10641937935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10641937935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17031295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17031295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10641937935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17031295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(y:sympy.Rational):
	#((y > sqrt(10845952935)/51200) | (y > -sqrt(17357719)/2048)) & ((y > sqrt(10845952935)/51200) | (y < -sqrt(10845952935)/51200)) & ((y > -sqrt(17357719)/2048) | (y < sqrt(17357719)/2048)) & ((y < -sqrt(10845952935)/51200) | (y < sqrt(17357719)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10845952935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17357719), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10845952935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10845952935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17357719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17357719), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10845952935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17357719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(y:sympy.Rational):
	#((y > 3*sqrt(1217619215)/51200) | (y > -sqrt(17537911)/2048)) & ((y > 3*sqrt(1217619215)/51200) | (y < -3*sqrt(1217619215)/51200)) & ((y > -sqrt(17537911)/2048) | (y < sqrt(17537911)/2048)) & ((y < -3*sqrt(1217619215)/51200) | (y < sqrt(17537911)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1217619215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17537911), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1217619215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1217619215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17537911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17537911), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1217619215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17537911), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(y:sympy.Rational):
	#((y > -sqrt(1059719)/512) | (y > sqrt(662160535)/12800)) & ((y > -sqrt(1059719)/512) | (y < sqrt(1059719)/512)) & ((y > sqrt(662160535)/12800) | (y < -sqrt(662160535)/12800)) & ((y < sqrt(1059719)/512) | (y < -sqrt(662160535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1059719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(662160535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1059719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1059719), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(662160535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(662160535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1059719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(662160535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(y:sympy.Rational):
	#((y > sqrt(2622064015)/25600) | (y > -sqrt(4196351)/1024)) & ((y > sqrt(2622064015)/25600) | (y < -sqrt(2622064015)/25600)) & ((y > -sqrt(4196351)/1024) | (y < sqrt(4196351)/1024)) & ((y < -sqrt(2622064015)/25600) | (y < sqrt(4196351)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2622064015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4196351), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2622064015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2622064015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4196351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4196351), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2622064015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4196351), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(y:sympy.Rational):
	#((y > 3*sqrt(1222229215)/51200) | (y > -sqrt(17604295)/2048)) & ((y > 3*sqrt(1222229215)/51200) | (y < -3*sqrt(1222229215)/51200)) & ((y > -sqrt(17604295)/2048) | (y < sqrt(17604295)/2048)) & ((y < -3*sqrt(1222229215)/51200) | (y < sqrt(17604295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1222229215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17604295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1222229215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1222229215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17604295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17604295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1222229215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17604295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(y:sympy.Rational):
	#((y > sqrt(16815)/1600) | (y > -sqrt(31)/64)) & ((y > sqrt(16815)/1600) | (y < -sqrt(16815)/1600)) & ((y > -sqrt(31)/64) | (y < sqrt(31)/64)) & ((y < -sqrt(16815)/1600) | (y < sqrt(31)/64))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(16815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(31), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(16815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(16815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(31), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(31), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(16815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(31), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(y:sympy.Rational):
	#((y > sqrt(10646897935)/51200) | (y > -sqrt(17039231)/2048)) & ((y > sqrt(10646897935)/51200) | (y < -sqrt(10646897935)/51200)) & ((y > -sqrt(17039231)/2048) | (y < sqrt(17039231)/2048)) & ((y < -sqrt(10646897935)/51200) | (y < sqrt(17039231)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10646897935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17039231), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10646897935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10646897935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17039231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17039231), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10646897935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17039231), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(y:sympy.Rational):
	#((y > sqrt(10766815)/1600) | (y > -sqrt(17231)/64)) & ((y > sqrt(10766815)/1600) | (y < -sqrt(10766815)/1600)) & ((y > -sqrt(17231)/64) | (y < sqrt(17231)/64)) & ((y < -sqrt(10766815)/1600) | (y < sqrt(17231)/64))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(10766815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17231), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(10766815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(10766815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17231), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(10766815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17231), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(y:sympy.Rational):
	#((y > sqrt(169058415)/6400) | (y > -sqrt(270559)/256)) & ((y > sqrt(169058415)/6400) | (y < -sqrt(169058415)/6400)) & ((y > -sqrt(270559)/256) | (y < sqrt(270559)/256)) & ((y < -sqrt(169058415)/6400) | (y < sqrt(270559)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(169058415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(270559), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(169058415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(169058415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(270559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(270559), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(169058415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(270559), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(y:sympy.Rational):
	#((y > 3*sqrt(1169044215)/51200) | (y > -sqrt(16838431)/2048)) & ((y > 3*sqrt(1169044215)/51200) | (y < -3*sqrt(1169044215)/51200)) & ((y > -sqrt(16838431)/2048) | (y < sqrt(16838431)/2048)) & ((y < -3*sqrt(1169044215)/51200) | (y < sqrt(16838431)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1169044215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16838431), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1169044215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1169044215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16838431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16838431), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1169044215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16838431), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(y:sympy.Rational):
	#((y > 3*sqrt(73850615)/12800) | (y > -11*sqrt(8791)/512)) & ((y > 3*sqrt(73850615)/12800) | (y < -3*sqrt(73850615)/12800)) & ((y > -11*sqrt(8791)/512) | (y < 11*sqrt(8791)/512)) & ((y < -3*sqrt(73850615)/12800) | (y < 11*sqrt(8791)/512))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(73850615), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 512), Pow(Integer(8791), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(73850615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(73850615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 512), Pow(Integer(8791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 512), Pow(Integer(8791), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(73850615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 512), Pow(Integer(8791), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(y:sympy.Rational):
	#((y > sqrt(10531552935)/51200) | (y > -sqrt(16854679)/2048)) & ((y > sqrt(10531552935)/51200) | (y < -sqrt(10531552935)/51200)) & ((y > -sqrt(16854679)/2048) | (y < sqrt(16854679)/2048)) & ((y < -sqrt(10531552935)/51200) | (y < sqrt(16854679)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10531552935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16854679), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10531552935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10531552935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16854679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16854679), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10531552935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16854679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(y:sympy.Rational):
	#((y > sqrt(11099777935)/51200) | (y > -sqrt(17763839)/2048)) & ((y > sqrt(11099777935)/51200) | (y < -sqrt(11099777935)/51200)) & ((y > -sqrt(17763839)/2048) | (y < sqrt(17763839)/2048)) & ((y < -sqrt(11099777935)/51200) | (y < sqrt(17763839)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11099777935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17763839), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11099777935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11099777935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17763839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17763839), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11099777935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17763839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(y:sympy.Rational):
	#((y > sqrt(11095297935)/51200) | (y > -sqrt(17756671)/2048)) & ((y > sqrt(11095297935)/51200) | (y < -sqrt(11095297935)/51200)) & ((y > -sqrt(17756671)/2048) | (y < sqrt(17756671)/2048)) & ((y < -sqrt(11095297935)/51200) | (y < sqrt(17756671)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11095297935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17756671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11095297935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11095297935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17756671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17756671), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11095297935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17756671), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(y:sympy.Rational):
	#((y > sqrt(252616335)/204800) | (y > -11*sqrt(3895)/8192)) & ((y > sqrt(252616335)/204800) | (y < -sqrt(252616335)/204800)) & ((y > -11*sqrt(3895)/8192) | (y < 11*sqrt(3895)/8192)) & ((y < -sqrt(252616335)/204800) | (y < 11*sqrt(3895)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(252616335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 8192), Pow(Integer(3895), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(252616335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(252616335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 8192), Pow(Integer(3895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 8192), Pow(Integer(3895), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(252616335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 8192), Pow(Integer(3895), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(y:sympy.Rational):
	#((y > -sqrt(1101871)/512) | (y > 3*sqrt(76500615)/12800)) & ((y > -sqrt(1101871)/512) | (y < sqrt(1101871)/512)) & ((y > 3*sqrt(76500615)/12800) | (y < -3*sqrt(76500615)/12800)) & ((y < sqrt(1101871)/512) | (y < -3*sqrt(76500615)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1101871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(76500615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1101871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1101871), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(76500615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(76500615), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1101871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(76500615), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(y:sympy.Rational):
	#((y > -sqrt(1110911)/512) | (y > sqrt(694155535)/12800)) & ((y > -sqrt(1110911)/512) | (y < sqrt(1110911)/512)) & ((y > sqrt(694155535)/12800) | (y < -sqrt(694155535)/12800)) & ((y < sqrt(1110911)/512) | (y < -sqrt(694155535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1110911), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(694155535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1110911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1110911), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(694155535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(694155535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1110911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(694155535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(y:sympy.Rational):
	#((y > 3*sqrt(1235789215)/51200) | (y > -sqrt(17799559)/2048)) & ((y > 3*sqrt(1235789215)/51200) | (y < -3*sqrt(1235789215)/51200)) & ((y > -sqrt(17799559)/2048) | (y < sqrt(17799559)/2048)) & ((y < -3*sqrt(1235789215)/51200) | (y < sqrt(17799559)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1235789215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17799559), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1235789215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1235789215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17799559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17799559), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1235789215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17799559), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(y:sympy.Rational):
	#((y > 3*sqrt(1217104215)/51200) | (y > -sqrt(17530495)/2048)) & ((y > 3*sqrt(1217104215)/51200) | (y < -3*sqrt(1217104215)/51200)) & ((y > -sqrt(17530495)/2048) | (y < sqrt(17530495)/2048)) & ((y < -3*sqrt(1217104215)/51200) | (y < sqrt(17530495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1217104215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17530495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1217104215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1217104215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17530495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17530495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1217104215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17530495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(y:sympy.Rational):
	#((y > sqrt(11032052935)/51200) | (y > -sqrt(17655479)/2048)) & ((y > sqrt(11032052935)/51200) | (y < -sqrt(11032052935)/51200)) & ((y > -sqrt(17655479)/2048) | (y < sqrt(17655479)/2048)) & ((y < -sqrt(11032052935)/51200) | (y < sqrt(17655479)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11032052935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17655479), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11032052935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11032052935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17655479), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17655479), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11032052935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17655479), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(y:sympy.Rational):
	#((y > -sqrt(145279)/4096) | (y > 3*sqrt(8923735)/102400)) & ((y > -sqrt(145279)/4096) | (y < sqrt(145279)/4096)) & ((y > 3*sqrt(8923735)/102400) | (y < -3*sqrt(8923735)/102400)) & ((y < sqrt(145279)/4096) | (y < -3*sqrt(8923735)/102400))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(145279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(3, 102400), Pow(Integer(8923735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(145279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(145279), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 102400), Pow(Integer(8923735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 102400), Pow(Integer(8923735), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(145279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 102400), Pow(Integer(8923735), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(y:sympy.Rational):
	#((y > sqrt(2768769015)/25600) | (y > -sqrt(4431079)/1024)) & ((y > sqrt(2768769015)/25600) | (y < -sqrt(2768769015)/25600)) & ((y > -sqrt(4431079)/1024) | (y < sqrt(4431079)/1024)) & ((y < -sqrt(2768769015)/25600) | (y < sqrt(4431079)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2768769015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4431079), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2768769015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2768769015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4431079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4431079), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2768769015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4431079), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(y:sympy.Rational):
	#((y > sqrt(11104252935)/51200) | (y > -sqrt(17770999)/2048)) & ((y > sqrt(11104252935)/51200) | (y < -sqrt(11104252935)/51200)) & ((y > -sqrt(17770999)/2048) | (y < sqrt(17770999)/2048)) & ((y < -sqrt(11104252935)/51200) | (y < sqrt(17770999)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11104252935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17770999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11104252935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11104252935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17770999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17770999), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11104252935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17770999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(y:sympy.Rational):
	#((y > sqrt(10949297935)/51200) | (y > -sqrt(17523071)/2048)) & ((y > sqrt(10949297935)/51200) | (y < -sqrt(10949297935)/51200)) & ((y > -sqrt(17523071)/2048) | (y < sqrt(17523071)/2048)) & ((y < -sqrt(10949297935)/51200) | (y < sqrt(17523071)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10949297935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17523071), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10949297935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10949297935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17523071), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17523071), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10949297935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17523071), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(y:sympy.Rational):
	#((y > sqrt(10850702935)/51200) | (y > -sqrt(17365319)/2048)) & ((y > sqrt(10850702935)/51200) | (y < -sqrt(10850702935)/51200)) & ((y > -sqrt(17365319)/2048) | (y < sqrt(17365319)/2048)) & ((y < -sqrt(10850702935)/51200) | (y < sqrt(17365319)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10850702935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17365319), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10850702935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10850702935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17365319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17365319), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10850702935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17365319), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(y:sympy.Rational):
	#((y > -sqrt(1109119)/512) | (y > sqrt(693035535)/12800)) & ((y > -sqrt(1109119)/512) | (y < sqrt(1109119)/512)) & ((y > sqrt(693035535)/12800) | (y < -sqrt(693035535)/12800)) & ((y < sqrt(1109119)/512) | (y < -sqrt(693035535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1109119), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(693035535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1109119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1109119), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(693035535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(693035535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1109119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(693035535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(y:sympy.Rational):
	#((y > -sqrt(1092631)/512) | (y > sqrt(682730535)/12800)) & ((y > -sqrt(1092631)/512) | (y < sqrt(1092631)/512)) & ((y > sqrt(682730535)/12800) | (y < -sqrt(682730535)/12800)) & ((y < sqrt(1092631)/512) | (y < -sqrt(682730535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1092631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(682730535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1092631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1092631), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(682730535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(682730535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1092631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(682730535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(y:sympy.Rational):
	#((y > sqrt(10636972935)/51200) | (y > -sqrt(17023351)/2048)) & ((y > sqrt(10636972935)/51200) | (y < -sqrt(10636972935)/51200)) & ((y > -sqrt(17023351)/2048) | (y < sqrt(17023351)/2048)) & ((y < -sqrt(10636972935)/51200) | (y < sqrt(17023351)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10636972935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17023351), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10636972935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10636972935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17023351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17023351), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10636972935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17023351), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(y:sympy.Rational):
	#((y > 9*sqrt(4248535)/204800) | (y > -sqrt(617719)/8192)) & ((y > 9*sqrt(4248535)/204800) | (y < -9*sqrt(4248535)/204800)) & ((y > -sqrt(617719)/8192) | (y < sqrt(617719)/8192)) & ((y < -9*sqrt(4248535)/204800) | (y < sqrt(617719)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 204800), Pow(Integer(4248535), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(617719), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 204800), Pow(Integer(4248535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 204800), Pow(Integer(4248535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(617719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(617719), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 204800), Pow(Integer(4248535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(617719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(y:sympy.Rational):
	#((y > sqrt(11090812935)/51200) | (y > -sqrt(17749495)/2048)) & ((y > sqrt(11090812935)/51200) | (y < -sqrt(11090812935)/51200)) & ((y > -sqrt(17749495)/2048) | (y < sqrt(17749495)/2048)) & ((y < -sqrt(11090812935)/51200) | (y < sqrt(17749495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11090812935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17749495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11090812935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11090812935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17749495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17749495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11090812935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17749495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(y:sympy.Rational):
	#((y > 3*sqrt(1231314215)/51200) | (y > -89*sqrt(2239)/2048)) & ((y > 3*sqrt(1231314215)/51200) | (y < -3*sqrt(1231314215)/51200)) & ((y > -89*sqrt(2239)/2048) | (y < 89*sqrt(2239)/2048)) & ((y < -3*sqrt(1231314215)/51200) | (y < 89*sqrt(2239)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1231314215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(89, 2048), Pow(Integer(2239), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1231314215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1231314215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(89, 2048), Pow(Integer(2239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(89, 2048), Pow(Integer(2239), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1231314215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(89, 2048), Pow(Integer(2239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(y:sympy.Rational):
	#((y > sqrt(2720364015)/25600) | (y > -sqrt(4353631)/1024)) & ((y > sqrt(2720364015)/25600) | (y < -sqrt(2720364015)/25600)) & ((y > -sqrt(4353631)/1024) | (y < sqrt(4353631)/1024)) & ((y < -sqrt(2720364015)/25600) | (y < sqrt(4353631)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2720364015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4353631), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2720364015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2720364015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4353631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4353631), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2720364015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4353631), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(y:sympy.Rational):
	#((y > -sqrt(16903231)/2048) | (y > 57*sqrt(3250815)/51200)) & ((y > -sqrt(16903231)/2048) | (y < sqrt(16903231)/2048)) & ((y > 57*sqrt(3250815)/51200) | (y < -57*sqrt(3250815)/51200)) & ((y < sqrt(16903231)/2048) | (y < -57*sqrt(3250815)/51200))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16903231), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(57, 51200), Pow(Integer(3250815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16903231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16903231), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(57, 51200), Pow(Integer(3250815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(57, 51200), Pow(Integer(3250815), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16903231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(57, 51200), Pow(Integer(3250815), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(y:sympy.Rational):
	#((y > sqrt(10617062935)/51200) | (y > -sqrt(16991495)/2048)) & ((y > sqrt(10617062935)/51200) | (y < -sqrt(10617062935)/51200)) & ((y > -sqrt(16991495)/2048) | (y < sqrt(16991495)/2048)) & ((y < -sqrt(10617062935)/51200) | (y < sqrt(16991495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10617062935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16991495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10617062935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10617062935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16991495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16991495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10617062935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16991495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(y:sympy.Rational):
	#((y > 29*sqrt(203815)/6400) | (y > -sqrt(274319)/256)) & ((y > 29*sqrt(203815)/6400) | (y < -29*sqrt(203815)/6400)) & ((y > -sqrt(274319)/256) | (y < sqrt(274319)/256)) & ((y < -29*sqrt(203815)/6400) | (y < sqrt(274319)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(29, 6400), Pow(Integer(203815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(274319), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(29, 6400), Pow(Integer(203815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(29, 6400), Pow(Integer(203815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(274319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(274319), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(29, 6400), Pow(Integer(203815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(274319), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(y:sympy.Rational):
	#((y > 9*sqrt(136757135)/51200) | (y > -sqrt(17727919)/2048)) & ((y > 9*sqrt(136757135)/51200) | (y < -9*sqrt(136757135)/51200)) & ((y > -sqrt(17727919)/2048) | (y < sqrt(17727919)/2048)) & ((y < -9*sqrt(136757135)/51200) | (y < sqrt(17727919)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 51200), Pow(Integer(136757135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17727919), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 51200), Pow(Integer(136757135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 51200), Pow(Integer(136757135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17727919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17727919), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 51200), Pow(Integer(136757135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17727919), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(y:sympy.Rational):
	#((y > sqrt(2741379015)/25600) | (y > -sqrt(4387255)/1024)) & ((y > sqrt(2741379015)/25600) | (y < -sqrt(2741379015)/25600)) & ((y > -sqrt(4387255)/1024) | (y < sqrt(4387255)/1024)) & ((y < -sqrt(2741379015)/25600) | (y < sqrt(4387255)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2741379015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4387255), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2741379015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2741379015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4387255), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4387255), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2741379015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4387255), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(y:sympy.Rational):
	#((y > sqrt(10841197935)/51200) | (y > -sqrt(17350111)/2048)) & ((y > sqrt(10841197935)/51200) | (y < -sqrt(10841197935)/51200)) & ((y > -sqrt(17350111)/2048) | (y < sqrt(17350111)/2048)) & ((y < -sqrt(10841197935)/51200) | (y < sqrt(17350111)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10841197935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17350111), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10841197935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10841197935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17350111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17350111), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10841197935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17350111), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(y:sympy.Rational):
	#((y > sqrt(298376335)/204800) | (y > -sqrt(544511)/8192)) & ((y > sqrt(298376335)/204800) | (y < -sqrt(298376335)/204800)) & ((y > -sqrt(544511)/8192) | (y < sqrt(544511)/8192)) & ((y < -sqrt(298376335)/204800) | (y < sqrt(544511)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(298376335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(544511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(298376335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(298376335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(544511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(544511), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(298376335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(544511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(y:sympy.Rational):
	#((y > sqrt(10541687935)/51200) | (y > -sqrt(16870895)/2048)) & ((y > sqrt(10541687935)/51200) | (y < -sqrt(10541687935)/51200)) & ((y > -sqrt(16870895)/2048) | (y < sqrt(16870895)/2048)) & ((y < -sqrt(10541687935)/51200) | (y < sqrt(16870895)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10541687935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16870895), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10541687935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10541687935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16870895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16870895), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10541687935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16870895), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(y:sympy.Rational):
	#((y > 3*sqrt(291624335)/25600) | (y > -sqrt(4200439)/1024)) & ((y > 3*sqrt(291624335)/25600) | (y < -3*sqrt(291624335)/25600)) & ((y > -sqrt(4200439)/1024) | (y < sqrt(4200439)/1024)) & ((y < -3*sqrt(291624335)/25600) | (y < sqrt(4200439)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(291624335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4200439), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(291624335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(291624335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4200439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4200439), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(291624335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4200439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(y:sympy.Rational):
	#((y > sqrt(11497935)/51200) | (y > -sqrt(22591)/2048)) & ((y > sqrt(11497935)/51200) | (y < -sqrt(11497935)/51200)) & ((y > -sqrt(22591)/2048) | (y < sqrt(22591)/2048)) & ((y < -sqrt(11497935)/51200) | (y < sqrt(22591)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11497935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(22591), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11497935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11497935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(22591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(22591), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11497935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(22591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(y:sympy.Rational):
	#((y > sqrt(10902622935)/51200) | (y > -sqrt(17448391)/2048)) & ((y > sqrt(10902622935)/51200) | (y < -sqrt(10902622935)/51200)) & ((y > -sqrt(17448391)/2048) | (y < sqrt(17448391)/2048)) & ((y < -sqrt(10902622935)/51200) | (y < sqrt(17448391)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10902622935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17448391), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10902622935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10902622935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17448391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17448391), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10902622935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17448391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(y:sympy.Rational):
	#((y > sqrt(10893227935)/51200) | (y > -sqrt(17433359)/2048)) & ((y > sqrt(10893227935)/51200) | (y < -sqrt(10893227935)/51200)) & ((y > -sqrt(17433359)/2048) | (y < sqrt(17433359)/2048)) & ((y < -sqrt(10893227935)/51200) | (y < sqrt(17433359)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10893227935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17433359), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10893227935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10893227935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17433359), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17433359), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10893227935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17433359), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(y:sympy.Rational):
	#((y > sqrt(2771019015)/25600) | (y > -sqrt(4434679)/1024)) & ((y > sqrt(2771019015)/25600) | (y < -sqrt(2771019015)/25600)) & ((y > -sqrt(4434679)/1024) | (y < sqrt(4434679)/1024)) & ((y < -sqrt(2771019015)/25600) | (y < sqrt(4434679)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2771019015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4434679), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2771019015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2771019015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4434679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4434679), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2771019015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4434679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(y:sympy.Rational):
	#((y > sqrt(42339135)/3200) | (y > -sqrt(67759)/128)) & ((y > sqrt(42339135)/3200) | (y < -sqrt(42339135)/3200)) & ((y > -sqrt(67759)/128) | (y < sqrt(67759)/128)) & ((y < -sqrt(42339135)/3200) | (y < sqrt(67759)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(42339135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67759), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(42339135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(42339135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67759), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(42339135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67759), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(y:sympy.Rational):
	#((y > sqrt(10860187935)/51200) | (y > -sqrt(17380495)/2048)) & ((y > sqrt(10860187935)/51200) | (y < -sqrt(10860187935)/51200)) & ((y > -sqrt(17380495)/2048) | (y < sqrt(17380495)/2048)) & ((y < -sqrt(10860187935)/51200) | (y < sqrt(17380495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10860187935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17380495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10860187935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10860187935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17380495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17380495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10860187935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17380495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(y:sympy.Rational):
	#((y > 3*sqrt(1179119215)/51200) | (y > -sqrt(16983511)/2048)) & ((y > 3*sqrt(1179119215)/51200) | (y < -3*sqrt(1179119215)/51200)) & ((y > -sqrt(16983511)/2048) | (y < sqrt(16983511)/2048)) & ((y < -3*sqrt(1179119215)/51200) | (y < sqrt(16983511)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1179119215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16983511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1179119215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1179119215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16983511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16983511), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1179119215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16983511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(y:sympy.Rational):
	#((y > sqrt(2639844015)/25600) | (y > -sqrt(4224799)/1024)) & ((y > sqrt(2639844015)/25600) | (y < -sqrt(2639844015)/25600)) & ((y > -sqrt(4224799)/1024) | (y < sqrt(4224799)/1024)) & ((y < -sqrt(2639844015)/25600) | (y < sqrt(4224799)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2639844015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4224799), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2639844015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2639844015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4224799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4224799), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2639844015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4224799), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(y:sympy.Rational):
	#((y > sqrt(206851335)/204800) | (y > -sqrt(398071)/8192)) & ((y > sqrt(206851335)/204800) | (y < -sqrt(206851335)/204800)) & ((y > -sqrt(398071)/8192) | (y < sqrt(398071)/8192)) & ((y < -sqrt(206851335)/204800) | (y < sqrt(398071)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(206851335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(398071), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(206851335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(206851335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(398071), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(398071), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(206851335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(398071), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(y:sympy.Rational):
	#((y > sqrt(11027497935)/51200) | (y > -sqrt(17648191)/2048)) & ((y > sqrt(11027497935)/51200) | (y < -sqrt(11027497935)/51200)) & ((y > -sqrt(17648191)/2048) | (y < sqrt(17648191)/2048)) & ((y < -sqrt(11027497935)/51200) | (y < sqrt(17648191)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11027497935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17648191), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11027497935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11027497935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17648191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17648191), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11027497935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17648191), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(y:sympy.Rational):
	#((y > 3*sqrt(18305935)/6400) | (y > -sqrt(263671)/256)) & ((y > 3*sqrt(18305935)/6400) | (y < -3*sqrt(18305935)/6400)) & ((y > -sqrt(263671)/256) | (y < sqrt(263671)/256)) & ((y < -3*sqrt(18305935)/6400) | (y < sqrt(263671)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18305935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(263671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18305935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18305935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(263671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(263671), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18305935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(263671), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(y:sympy.Rational):
	#((y > sqrt(161081335)/204800) | (y > -sqrt(324839)/8192)) & ((y > sqrt(161081335)/204800) | (y < -sqrt(161081335)/204800)) & ((y > -sqrt(324839)/8192) | (y < sqrt(324839)/8192)) & ((y < -sqrt(161081335)/204800) | (y < sqrt(324839)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(161081335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(324839), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(161081335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(161081335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(324839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(324839), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(161081335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(324839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(y:sympy.Rational):
	#((y > -sqrt(1090759)/512) | (y > sqrt(681560535)/12800)) & ((y > -sqrt(1090759)/512) | (y < sqrt(1090759)/512)) & ((y > sqrt(681560535)/12800) | (y < -sqrt(681560535)/12800)) & ((y < sqrt(1090759)/512) | (y < -sqrt(681560535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1090759), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(681560535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1090759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1090759), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(681560535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(681560535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1090759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(681560535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(y:sympy.Rational):
	#((y > sqrt(2710894015)/25600) | (y > -sqrt(4338479)/1024)) & ((y > sqrt(2710894015)/25600) | (y < -sqrt(2710894015)/25600)) & ((y > -sqrt(4338479)/1024) | (y < sqrt(4338479)/1024)) & ((y < -sqrt(2710894015)/25600) | (y < sqrt(4338479)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2710894015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4338479), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2710894015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2710894015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4338479), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4338479), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2710894015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4338479), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(y:sympy.Rational):
	#((y > sqrt(173118415)/6400) | (y > -sqrt(277055)/256)) & ((y > sqrt(173118415)/6400) | (y < -sqrt(173118415)/6400)) & ((y > -sqrt(277055)/256) | (y < sqrt(277055)/256)) & ((y < -sqrt(173118415)/6400) | (y < sqrt(277055)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(173118415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277055), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(173118415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(173118415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277055), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277055), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(173118415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277055), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(y:sympy.Rational):
	#((y > sqrt(10632002935)/51200) | (y > -sqrt(17015399)/2048)) & ((y > sqrt(10632002935)/51200) | (y < -sqrt(10632002935)/51200)) & ((y > -sqrt(17015399)/2048) | (y < sqrt(17015399)/2048)) & ((y < -sqrt(10632002935)/51200) | (y < sqrt(17015399)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10632002935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17015399), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10632002935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10632002935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17015399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17015399), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10632002935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17015399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(y:sympy.Rational):
	#((y > sqrt(10622047935)/51200) | (y > -sqrt(16999471)/2048)) & ((y > sqrt(10622047935)/51200) | (y < -sqrt(10622047935)/51200)) & ((y > -sqrt(16999471)/2048) | (y < sqrt(16999471)/2048)) & ((y < -sqrt(10622047935)/51200) | (y < sqrt(16999471)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10622047935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16999471), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10622047935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10622047935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16999471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16999471), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10622047935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16999471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(y:sympy.Rational):
	#((y > -sqrt(1107319)/512) | (y > sqrt(691910535)/12800)) & ((y > -sqrt(1107319)/512) | (y < sqrt(1107319)/512)) & ((y > sqrt(691910535)/12800) | (y < -sqrt(691910535)/12800)) & ((y < sqrt(1107319)/512) | (y < -sqrt(691910535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1107319), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(691910535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1107319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1107319), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(691910535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(691910535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1107319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(691910535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(y:sympy.Rational):
	#((y > -sqrt(16822151)/2048) | (y > 43*sqrt(5684815)/51200)) & ((y > -sqrt(16822151)/2048) | (y < sqrt(16822151)/2048)) & ((y > 43*sqrt(5684815)/51200) | (y < -43*sqrt(5684815)/51200)) & ((y < sqrt(16822151)/2048) | (y < -43*sqrt(5684815)/51200))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16822151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(43, 51200), Pow(Integer(5684815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(16822151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16822151), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(43, 51200), Pow(Integer(5684815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(43, 51200), Pow(Integer(5684815), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(16822151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(43, 51200), Pow(Integer(5684815), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(y:sympy.Rational):
	#((y > sqrt(2652394015)/25600) | (y > -sqrt(4244879)/1024)) & ((y > sqrt(2652394015)/25600) | (y < -sqrt(2652394015)/25600)) & ((y > -sqrt(4244879)/1024) | (y < sqrt(4244879)/1024)) & ((y < -sqrt(2652394015)/25600) | (y < sqrt(4244879)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2652394015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4244879), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2652394015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2652394015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4244879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4244879), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2652394015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4244879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(y:sympy.Rational):
	#((y > sqrt(10316815)/1600) | (y > -sqrt(16511)/64)) & ((y > sqrt(10316815)/1600) | (y < -sqrt(10316815)/1600)) & ((y > -sqrt(16511)/64) | (y < sqrt(16511)/64)) & ((y < -sqrt(10316815)/1600) | (y < sqrt(16511)/64))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(10316815), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 1600), Pow(Integer(10316815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(10316815), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16511), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1600), Pow(Integer(10316815), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(y:sympy.Rational):
	#((y > sqrt(10926022935)/51200) | (y > -11*sqrt(144511)/2048)) & ((y > sqrt(10926022935)/51200) | (y < -sqrt(10926022935)/51200)) & ((y > -11*sqrt(144511)/2048) | (y < 11*sqrt(144511)/2048)) & ((y < -sqrt(10926022935)/51200) | (y < 11*sqrt(144511)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10926022935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 2048), Pow(Integer(144511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10926022935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10926022935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 2048), Pow(Integer(144511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 2048), Pow(Integer(144511), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10926022935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 2048), Pow(Integer(144511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(y:sympy.Rational):
	#((y > sqrt(10864922935)/51200) | (y > -sqrt(17388071)/2048)) & ((y > sqrt(10864922935)/51200) | (y < -sqrt(10864922935)/51200)) & ((y > -sqrt(17388071)/2048) | (y < sqrt(17388071)/2048)) & ((y < -sqrt(10864922935)/51200) | (y < sqrt(17388071)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10864922935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17388071), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10864922935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10864922935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17388071), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17388071), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10864922935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17388071), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(y:sympy.Rational):
	#((y > sqrt(11054752935)/51200) | (y > -sqrt(17691799)/2048)) & ((y > sqrt(11054752935)/51200) | (y < -sqrt(11054752935)/51200)) & ((y > -sqrt(17691799)/2048) | (y < sqrt(17691799)/2048)) & ((y < -sqrt(11054752935)/51200) | (y < sqrt(17691799)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11054752935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17691799), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11054752935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11054752935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17691799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17691799), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11054752935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17691799), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(y:sympy.Rational):
	#((y > sqrt(166008415)/6400) | (y > -sqrt(265679)/256)) & ((y > sqrt(166008415)/6400) | (y < -sqrt(166008415)/6400)) & ((y > -sqrt(265679)/256) | (y < sqrt(265679)/256)) & ((y < -sqrt(166008415)/6400) | (y < sqrt(265679)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(166008415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(265679), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(166008415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(166008415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(265679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(265679), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(166008415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(265679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(y:sympy.Rational):
	#((y > sqrt(10963202935)/51200) | (y > -sqrt(17545319)/2048)) & ((y > sqrt(10963202935)/51200) | (y < -sqrt(10963202935)/51200)) & ((y > -sqrt(17545319)/2048) | (y < sqrt(17545319)/2048)) & ((y < -sqrt(10963202935)/51200) | (y < sqrt(17545319)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10963202935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17545319), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10963202935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10963202935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17545319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17545319), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10963202935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17545319), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(y:sympy.Rational):
	#((y > -sqrt(1061719)/512) | (y > sqrt(663410535)/12800)) & ((y > -sqrt(1061719)/512) | (y < sqrt(1061719)/512)) & ((y > sqrt(663410535)/12800) | (y < -sqrt(663410535)/12800)) & ((y < sqrt(1061719)/512) | (y < -sqrt(663410535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1061719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(663410535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1061719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1061719), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(663410535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(663410535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1061719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(663410535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(y:sympy.Rational):
	#((y > sqrt(2627169015)/25600) | (y > -sqrt(4204519)/1024)) & ((y > sqrt(2627169015)/25600) | (y < -sqrt(2627169015)/25600)) & ((y > -sqrt(4204519)/1024) | (y < sqrt(4204519)/1024)) & ((y < -sqrt(2627169015)/25600) | (y < sqrt(4204519)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2627169015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4204519), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2627169015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2627169015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4204519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4204519), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2627169015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4204519), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(y:sympy.Rational):
	#((y > sqrt(11068312935)/51200) | (y > -sqrt(17713495)/2048)) & ((y > sqrt(11068312935)/51200) | (y < -sqrt(11068312935)/51200)) & ((y > -sqrt(17713495)/2048) | (y < sqrt(17713495)/2048)) & ((y < -sqrt(11068312935)/51200) | (y < sqrt(17713495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11068312935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17713495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11068312935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11068312935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17713495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17713495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11068312935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17713495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(y:sympy.Rational):
	#((y > -sqrt(1051639)/512) | (y > sqrt(657110535)/12800)) & ((y > -sqrt(1051639)/512) | (y < sqrt(1051639)/512)) & ((y > sqrt(657110535)/12800) | (y < -sqrt(657110535)/12800)) & ((y < sqrt(1051639)/512) | (y < -sqrt(657110535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1051639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(657110535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1051639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1051639), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(657110535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(657110535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1051639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(657110535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(y:sympy.Rational):
	#((y > -sqrt(4279)/2048) | (y > sqrt(52935)/51200)) & ((y > -sqrt(4279)/2048) | (y < sqrt(4279)/2048)) & ((y > sqrt(52935)/51200) | (y < -sqrt(52935)/51200)) & ((y < sqrt(4279)/2048) | (y < -sqrt(52935)/51200))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(4279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(52935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(4279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(4279), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(52935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(52935), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(4279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(52935), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(y:sympy.Rational):
	#((y > sqrt(11072822935)/51200) | (y > -29*sqrt(21071)/2048)) & ((y > sqrt(11072822935)/51200) | (y < -sqrt(11072822935)/51200)) & ((y > -29*sqrt(21071)/2048) | (y < 29*sqrt(21071)/2048)) & ((y < -sqrt(11072822935)/51200) | (y < 29*sqrt(21071)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11072822935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(29, 2048), Pow(Integer(21071), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11072822935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11072822935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(29, 2048), Pow(Integer(21071), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(29, 2048), Pow(Integer(21071), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11072822935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(29, 2048), Pow(Integer(21071), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(y:sympy.Rational):
	#((y > 3*sqrt(18980935)/6400) | (y > -sqrt(273391)/256)) & ((y > 3*sqrt(18980935)/6400) | (y < -3*sqrt(18980935)/6400)) & ((y > -sqrt(273391)/256) | (y < sqrt(273391)/256)) & ((y < -3*sqrt(18980935)/6400) | (y < sqrt(273391)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18980935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(273391), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18980935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18980935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(273391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(273391), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18980935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(273391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(y:sympy.Rational):
	#((y > sqrt(2654889015)/25600) | (y > -sqrt(4248871)/1024)) & ((y > sqrt(2654889015)/25600) | (y < -sqrt(2654889015)/25600)) & ((y > -sqrt(4248871)/1024) | (y < sqrt(4248871)/1024)) & ((y < -sqrt(2654889015)/25600) | (y < sqrt(4248871)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2654889015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4248871), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2654889015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2654889015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4248871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4248871), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2654889015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4248871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(y:sympy.Rational):
	#((y > 3*sqrt(1221719215)/51200) | (y > -sqrt(17596951)/2048)) & ((y > 3*sqrt(1221719215)/51200) | (y < -3*sqrt(1221719215)/51200)) & ((y > -sqrt(17596951)/2048) | (y < sqrt(17596951)/2048)) & ((y < -3*sqrt(1221719215)/51200) | (y < sqrt(17596951)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1221719215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17596951), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1221719215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1221719215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17596951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17596951), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1221719215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17596951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(y:sympy.Rational):
	#((y > sqrt(10627027935)/51200) | (y > -sqrt(17007439)/2048)) & ((y > sqrt(10627027935)/51200) | (y < -sqrt(10627027935)/51200)) & ((y > -sqrt(17007439)/2048) | (y < sqrt(17007439)/2048)) & ((y < -sqrt(10627027935)/51200) | (y < sqrt(17007439)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10627027935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17007439), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10627027935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10627027935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17007439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17007439), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10627027935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17007439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(y:sympy.Rational):
	#((y > sqrt(11050222935)/51200) | (y > -sqrt(17684551)/2048)) & ((y > sqrt(11050222935)/51200) | (y < -sqrt(11050222935)/51200)) & ((y > -sqrt(17684551)/2048) | (y < sqrt(17684551)/2048)) & ((y < -sqrt(11050222935)/51200) | (y < sqrt(17684551)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11050222935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17684551), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11050222935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11050222935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17684551), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17684551), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11050222935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17684551), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(y:sympy.Rational):
	#((y > -sqrt(178351)/8192) | (y > sqrt(69526335)/204800)) & ((y > -sqrt(178351)/8192) | (y < sqrt(178351)/8192)) & ((y > sqrt(69526335)/204800) | (y < -sqrt(69526335)/204800)) & ((y < sqrt(178351)/8192) | (y < -sqrt(69526335)/204800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(178351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(69526335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(178351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(178351), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(69526335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(69526335), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(178351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(69526335), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(y:sympy.Rational):
	#((y > 3*sqrt(4801015)/3200) | (y > -sqrt(69151)/128)) & ((y > 3*sqrt(4801015)/3200) | (y < -3*sqrt(4801015)/3200)) & ((y > -sqrt(69151)/128) | (y < sqrt(69151)/128)) & ((y < -3*sqrt(4801015)/3200) | (y < sqrt(69151)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 3200), Pow(Integer(4801015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69151), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 3200), Pow(Integer(4801015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 3200), Pow(Integer(4801015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69151), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 3200), Pow(Integer(4801015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69151), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(y:sympy.Rational):
	#((y > sqrt(41109135)/3200) | (y > -sqrt(65791)/128)) & ((y > sqrt(41109135)/3200) | (y < -sqrt(41109135)/3200)) & ((y > -sqrt(65791)/128) | (y < sqrt(65791)/128)) & ((y < -sqrt(41109135)/3200) | (y < sqrt(65791)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(41109135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(65791), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(41109135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(41109135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(65791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(65791), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(41109135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(65791), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(y:sympy.Rational):
	#((y > sqrt(1444015)/25600) | (y > -sqrt(3359)/1024)) & ((y > sqrt(1444015)/25600) | (y < -sqrt(1444015)/25600)) & ((y > -sqrt(3359)/1024) | (y < sqrt(3359)/1024)) & ((y < -sqrt(1444015)/25600) | (y < sqrt(3359)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(1444015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(3359), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(1444015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(1444015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(3359), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(3359), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(1444015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(3359), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(y:sympy.Rational):
	#((y > -sqrt(1055695)/512) | (y > sqrt(659645535)/12800)) & ((y > -sqrt(1055695)/512) | (y < sqrt(1055695)/512)) & ((y > sqrt(659645535)/12800) | (y < -sqrt(659645535)/12800)) & ((y < sqrt(1055695)/512) | (y < -sqrt(659645535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1055695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(659645535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1055695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1055695), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(659645535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(659645535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1055695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(659645535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(y:sympy.Rational):
	#((y > -sqrt(1053671)/512) | (y > sqrt(658380535)/12800)) & ((y > -sqrt(1053671)/512) | (y < sqrt(1053671)/512)) & ((y > sqrt(658380535)/12800) | (y < -sqrt(658380535)/12800)) & ((y < sqrt(1053671)/512) | (y < -sqrt(658380535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1053671), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(658380535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1053671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1053671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(658380535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(658380535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1053671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(658380535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(y:sympy.Rational):
	#((y > 3*sqrt(292754335)/25600) | (y > -sqrt(4216711)/1024)) & ((y > 3*sqrt(292754335)/25600) | (y < -3*sqrt(292754335)/25600)) & ((y > -sqrt(4216711)/1024) | (y < sqrt(4216711)/1024)) & ((y < -3*sqrt(292754335)/25600) | (y < sqrt(4216711)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(292754335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4216711), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(292754335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(292754335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4216711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4216711), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(292754335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4216711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(y:sympy.Rational):
	#((y > 3*sqrt(1212964215)/51200) | (y > -sqrt(17470879)/2048)) & ((y > 3*sqrt(1212964215)/51200) | (y < -3*sqrt(1212964215)/51200)) & ((y > -sqrt(17470879)/2048) | (y < sqrt(17470879)/2048)) & ((y < -3*sqrt(1212964215)/51200) | (y < sqrt(17470879)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1212964215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17470879), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1212964215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1212964215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17470879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17470879), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1212964215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17470879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(y:sympy.Rational):
	#((y > sqrt(11063797935)/51200) | (y > -sqrt(17706271)/2048)) & ((y > sqrt(11063797935)/51200) | (y < -sqrt(11063797935)/51200)) & ((y > -sqrt(17706271)/2048) | (y < sqrt(17706271)/2048)) & ((y < -sqrt(11063797935)/51200) | (y < sqrt(17706271)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11063797935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17706271), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11063797935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11063797935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17706271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17706271), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11063797935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17706271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(y:sympy.Rational):
	#((y > sqrt(10986277935)/51200) | (y > -sqrt(17582239)/2048)) & ((y > sqrt(10986277935)/51200) | (y < -sqrt(10986277935)/51200)) & ((y > -sqrt(17582239)/2048) | (y < sqrt(17582239)/2048)) & ((y < -sqrt(10986277935)/51200) | (y < sqrt(17582239)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10986277935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17582239), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10986277935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10986277935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17582239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17582239), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10986277935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17582239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(y:sympy.Rational):
	#((y > 3*sqrt(307139335)/25600) | (y > -sqrt(4423855)/1024)) & ((y > 3*sqrt(307139335)/25600) | (y < -3*sqrt(307139335)/25600)) & ((y > -sqrt(4423855)/1024) | (y < sqrt(4423855)/1024)) & ((y < -3*sqrt(307139335)/25600) | (y < sqrt(4423855)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(307139335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4423855), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(307139335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(307139335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4423855), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4423855), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(307139335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4423855), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(y:sympy.Rational):
	#((y > 9*sqrt(1423535)/204800) | (y > -sqrt(251599)/8192)) & ((y > 9*sqrt(1423535)/204800) | (y < -9*sqrt(1423535)/204800)) & ((y > -sqrt(251599)/8192) | (y < sqrt(251599)/8192)) & ((y < -9*sqrt(1423535)/204800) | (y < sqrt(251599)/8192))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 204800), Pow(Integer(1423535), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(251599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 204800), Pow(Integer(1423535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 204800), Pow(Integer(1423535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(251599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(251599), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 204800), Pow(Integer(1423535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(251599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(y:sympy.Rational):
	#((y > sqrt(2629714015)/25600) | (y > -sqrt(4208591)/1024)) & ((y > sqrt(2629714015)/25600) | (y < -sqrt(2629714015)/25600)) & ((y > -sqrt(4208591)/1024) | (y < sqrt(4208591)/1024)) & ((y < -sqrt(2629714015)/25600) | (y < sqrt(4208591)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2629714015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4208591), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2629714015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2629714015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4208591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4208591), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2629714015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4208591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(y:sympy.Rational):
	#((y > sqrt(2632254015)/25600) | (y > -sqrt(4212655)/1024)) & ((y > sqrt(2632254015)/25600) | (y < -sqrt(2632254015)/25600)) & ((y > -sqrt(4212655)/1024) | (y < sqrt(4212655)/1024)) & ((y < -sqrt(2632254015)/25600) | (y < sqrt(4212655)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2632254015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4212655), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2632254015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2632254015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4212655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4212655), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2632254015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4212655), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(y:sympy.Rational):
	#((y > sqrt(11059277935)/51200) | (y > -sqrt(17699039)/2048)) & ((y > sqrt(11059277935)/51200) | (y < -sqrt(11059277935)/51200)) & ((y > -sqrt(17699039)/2048) | (y < sqrt(17699039)/2048)) & ((y < -sqrt(11059277935)/51200) | (y < sqrt(17699039)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11059277935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17699039), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11059277935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11059277935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17699039), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17699039), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11059277935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17699039), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(y:sympy.Rational):
	#((y > -sqrt(1105511)/512) | (y > sqrt(690780535)/12800)) & ((y > -sqrt(1105511)/512) | (y < sqrt(1105511)/512)) & ((y > sqrt(690780535)/12800) | (y < -sqrt(690780535)/12800)) & ((y < sqrt(1105511)/512) | (y < -sqrt(690780535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1105511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(690780535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1105511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1105511), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(690780535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(690780535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1105511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(690780535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(y:sympy.Rational):
	#((y > -sqrt(1073551)/512) | (y > sqrt(670805535)/12800)) & ((y > -sqrt(1073551)/512) | (y < sqrt(1073551)/512)) & ((y > sqrt(670805535)/12800) | (y < -sqrt(670805535)/12800)) & ((y < sqrt(1073551)/512) | (y < -sqrt(670805535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1073551), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(670805535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1073551), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1073551), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(670805535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(670805535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1073551), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(670805535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(y:sympy.Rational):
	#((y > sqrt(2761989015)/25600) | (y > -sqrt(4420231)/1024)) & ((y > sqrt(2761989015)/25600) | (y < -sqrt(2761989015)/25600)) & ((y > -sqrt(4420231)/1024) | (y < sqrt(4420231)/1024)) & ((y < -sqrt(2761989015)/25600) | (y < sqrt(4420231)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2761989015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4420231), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2761989015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2761989015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4420231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4420231), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2761989015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4420231), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(y:sympy.Rational):
	#((y > sqrt(10691312935)/51200) | (y > -sqrt(17110295)/2048)) & ((y > sqrt(10691312935)/51200) | (y < -sqrt(10691312935)/51200)) & ((y > -sqrt(17110295)/2048) | (y < sqrt(17110295)/2048)) & ((y < -sqrt(10691312935)/51200) | (y < sqrt(17110295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10691312935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17110295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10691312935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10691312935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17110295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17110295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10691312935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17110295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(y:sympy.Rational):
	#((y > sqrt(10774102935)/51200) | (y > -sqrt(17242759)/2048)) & ((y > sqrt(10774102935)/51200) | (y < -sqrt(10774102935)/51200)) & ((y > -sqrt(17242759)/2048) | (y < sqrt(17242759)/2048)) & ((y < -sqrt(10774102935)/51200) | (y < sqrt(17242759)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10774102935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17242759), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10774102935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10774102935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17242759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17242759), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10774102935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17242759), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(y:sympy.Rational):
	#((y > sqrt(10710922935)/51200) | (y > -sqrt(17141671)/2048)) & ((y > sqrt(10710922935)/51200) | (y < -sqrt(10710922935)/51200)) & ((y > -sqrt(17141671)/2048) | (y < sqrt(17141671)/2048)) & ((y < -sqrt(10710922935)/51200) | (y < sqrt(17141671)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10710922935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17141671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10710922935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10710922935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17141671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17141671), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10710922935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17141671), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(y:sympy.Rational):
	#((y > sqrt(10907312935)/51200) | (y > -sqrt(17455895)/2048)) & ((y > sqrt(10907312935)/51200) | (y < -sqrt(10907312935)/51200)) & ((y > -sqrt(17455895)/2048) | (y < sqrt(17455895)/2048)) & ((y < -sqrt(10907312935)/51200) | (y < sqrt(17455895)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10907312935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17455895), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10907312935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10907312935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17455895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17455895), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10907312935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17455895), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(y:sympy.Rational):
	#((y > sqrt(11045687935)/51200) | (y > -sqrt(17677295)/2048)) & ((y > sqrt(11045687935)/51200) | (y < -sqrt(11045687935)/51200)) & ((y > -sqrt(17677295)/2048) | (y < sqrt(17677295)/2048)) & ((y < -sqrt(11045687935)/51200) | (y < sqrt(17677295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11045687935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17677295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11045687935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11045687935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17677295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17677295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11045687935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17677295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(y:sympy.Rational):
	#((y > sqrt(10967827935)/51200) | (y > -sqrt(17552719)/2048)) & ((y > sqrt(10967827935)/51200) | (y < -sqrt(10967827935)/51200)) & ((y > -sqrt(17552719)/2048) | (y < sqrt(17552719)/2048)) & ((y < -sqrt(10967827935)/51200) | (y < sqrt(17552719)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10967827935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17552719), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10967827935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10967827935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17552719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17552719), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10967827935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17552719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(y:sympy.Rational):
	#((y > 3*sqrt(1189014215)/51200) | (y > -sqrt(17125999)/2048)) & ((y > 3*sqrt(1189014215)/51200) | (y < -3*sqrt(1189014215)/51200)) & ((y > -sqrt(17125999)/2048) | (y < sqrt(17125999)/2048)) & ((y < -3*sqrt(1189014215)/51200) | (y < sqrt(17125999)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1189014215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17125999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1189014215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1189014215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17125999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17125999), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1189014215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17125999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(y:sympy.Rational):
	#((y > 3*sqrt(306129335)/25600) | (y > -sqrt(4409311)/1024)) & ((y > 3*sqrt(306129335)/25600) | (y < -3*sqrt(306129335)/25600)) & ((y > -sqrt(4409311)/1024) | (y < sqrt(4409311)/1024)) & ((y < -3*sqrt(306129335)/25600) | (y < sqrt(4409311)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(306129335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4409311), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(306129335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(306129335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4409311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4409311), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(306129335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4409311), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(y:sympy.Rational):
	#((y > sqrt(10793372935)/51200) | (y > -sqrt(17273591)/2048)) & ((y > sqrt(10793372935)/51200) | (y < -sqrt(10793372935)/51200)) & ((y > -sqrt(17273591)/2048) | (y < sqrt(17273591)/2048)) & ((y < -sqrt(10793372935)/51200) | (y < sqrt(17273591)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10793372935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17273591), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10793372935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10793372935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17273591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17273591), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10793372935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17273591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(y:sympy.Rational):
	#((y > sqrt(10977062935)/51200) | (y > -sqrt(17567495)/2048)) & ((y > sqrt(10977062935)/51200) | (y < -sqrt(10977062935)/51200)) & ((y > -sqrt(17567495)/2048) | (y < sqrt(17567495)/2048)) & ((y < -sqrt(10977062935)/51200) | (y < sqrt(17567495)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10977062935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17567495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10977062935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10977062935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17567495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17567495), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10977062935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17567495), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(y:sympy.Rational):
	#((y > sqrt(2745994015)/25600) | (y > -sqrt(4394639)/1024)) & ((y > sqrt(2745994015)/25600) | (y < -sqrt(2745994015)/25600)) & ((y > -sqrt(4394639)/1024) | (y < sqrt(4394639)/1024)) & ((y < -sqrt(2745994015)/25600) | (y < sqrt(4394639)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2745994015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4394639), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2745994015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2745994015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4394639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4394639), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2745994015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4394639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(y:sympy.Rational):
	#((y > sqrt(11658615)/102400) | (y > -sqrt(35431)/4096)) & ((y > sqrt(11658615)/102400) | (y < -sqrt(11658615)/102400)) & ((y > -sqrt(35431)/4096) | (y < sqrt(35431)/4096)) & ((y < -sqrt(11658615)/102400) | (y < sqrt(35431)/4096))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(11658615), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(35431), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 102400), Pow(Integer(11658615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(11658615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4096), Pow(Integer(35431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(35431), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 102400), Pow(Integer(11658615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 4096), Pow(Integer(35431), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(y:sympy.Rational):
	#((y > sqrt(42924135)/3200) | (y > -sqrt(68695)/128)) & ((y > sqrt(42924135)/3200) | (y < -sqrt(42924135)/3200)) & ((y > -sqrt(68695)/128) | (y < sqrt(68695)/128)) & ((y < -sqrt(42924135)/3200) | (y < sqrt(68695)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(42924135), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(68695), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 3200), Pow(Integer(42924135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(42924135), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(68695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(68695), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 3200), Pow(Integer(42924135), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(68695), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(y:sympy.Rational):
	#((y > sqrt(171983415)/6400) | (y > -sqrt(275239)/256)) & ((y > sqrt(171983415)/6400) | (y < -sqrt(171983415)/6400)) & ((y > -sqrt(275239)/256) | (y < sqrt(275239)/256)) & ((y < -sqrt(171983415)/6400) | (y < sqrt(275239)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(171983415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(275239), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(171983415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(171983415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(275239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(275239), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(171983415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(275239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(y:sympy.Rational):
	#((y > sqrt(10990877935)/51200) | (y > -sqrt(17589599)/2048)) & ((y > sqrt(10990877935)/51200) | (y < -sqrt(10990877935)/51200)) & ((y > -sqrt(17589599)/2048) | (y < sqrt(17589599)/2048)) & ((y < -sqrt(10990877935)/51200) | (y < sqrt(17589599)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10990877935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17589599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10990877935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10990877935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17589599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17589599), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10990877935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17589599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(y:sympy.Rational):
	#((y > sqrt(2752879015)/25600) | (y > -sqrt(4405655)/1024)) & ((y > sqrt(2752879015)/25600) | (y < -sqrt(2752879015)/25600)) & ((y > -sqrt(4405655)/1024) | (y < sqrt(4405655)/1024)) & ((y < -sqrt(2752879015)/25600) | (y < sqrt(4405655)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2752879015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4405655), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2752879015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2752879015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4405655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4405655), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2752879015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4405655), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(y:sympy.Rational):
	#((y > -sqrt(105095)/8192) | (y > sqrt(23741335)/204800)) & ((y > -sqrt(105095)/8192) | (y < sqrt(105095)/8192)) & ((y > sqrt(23741335)/204800) | (y < -sqrt(23741335)/204800)) & ((y < sqrt(105095)/8192) | (y < -sqrt(23741335)/204800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(105095), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(23741335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8192), Pow(Integer(105095), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(105095), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 204800), Pow(Integer(23741335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(23741335), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 8192), Pow(Integer(105095), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 204800), Pow(Integer(23741335), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(y:sympy.Rational):
	#((y > sqrt(11009227935)/51200) | (y > -sqrt(17618959)/2048)) & ((y > sqrt(11009227935)/51200) | (y < -sqrt(11009227935)/51200)) & ((y > -sqrt(17618959)/2048) | (y < sqrt(17618959)/2048)) & ((y < -sqrt(11009227935)/51200) | (y < sqrt(17618959)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11009227935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17618959), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11009227935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11009227935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17618959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17618959), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11009227935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17618959), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(y:sympy.Rational):
	#((y > sqrt(11004647935)/51200) | (y > -sqrt(17611631)/2048)) & ((y > sqrt(11004647935)/51200) | (y < -sqrt(11004647935)/51200)) & ((y > -sqrt(17611631)/2048) | (y < sqrt(17611631)/2048)) & ((y < -sqrt(11004647935)/51200) | (y < sqrt(17611631)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11004647935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17611631), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(11004647935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11004647935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17611631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17611631), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(11004647935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17611631), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(y:sympy.Rational):
	#((y > -sqrt(1075495)/512) | (y > sqrt(672020535)/12800)) & ((y > -sqrt(1075495)/512) | (y < sqrt(1075495)/512)) & ((y > sqrt(672020535)/12800) | (y < -sqrt(672020535)/12800)) & ((y < sqrt(1075495)/512) | (y < -sqrt(672020535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1075495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(672020535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1075495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1075495), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(672020535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(672020535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1075495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(672020535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(y:sympy.Rational):
	#((y > sqrt(2667289015)/25600) | (y > -sqrt(4268711)/1024)) & ((y > sqrt(2667289015)/25600) | (y < -sqrt(2667289015)/25600)) & ((y > -sqrt(4268711)/1024) | (y < sqrt(4268711)/1024)) & ((y < -sqrt(2667289015)/25600) | (y < sqrt(4268711)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2667289015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4268711), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2667289015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2667289015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4268711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4268711), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2667289015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4268711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(y:sympy.Rational):
	#((y > 111*sqrt(220215)/25600) | (y > -sqrt(4342279)/1024)) & ((y > 111*sqrt(220215)/25600) | (y < -111*sqrt(220215)/25600)) & ((y > -sqrt(4342279)/1024) | (y < sqrt(4342279)/1024)) & ((y < -111*sqrt(220215)/25600) | (y < sqrt(4342279)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(111, 25600), Pow(Integer(220215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4342279), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(111, 25600), Pow(Integer(220215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(111, 25600), Pow(Integer(220215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4342279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4342279), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(111, 25600), Pow(Integer(220215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4342279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(y:sympy.Rational):
	#((y > 3*sqrt(296639335)/25600) | (y > -sqrt(4272655)/1024)) & ((y > 3*sqrt(296639335)/25600) | (y < -3*sqrt(296639335)/25600)) & ((y > -sqrt(4272655)/1024) | (y < sqrt(4272655)/1024)) & ((y < -3*sqrt(296639335)/25600) | (y < sqrt(4272655)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(296639335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4272655), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(296639335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(296639335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4272655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4272655), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(296639335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4272655), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(y:sympy.Rational):
	#((y > sqrt(10720697935)/51200) | (y > -sqrt(17157311)/2048)) & ((y > sqrt(10720697935)/51200) | (y < -sqrt(10720697935)/51200)) & ((y > -sqrt(17157311)/2048) | (y < sqrt(17157311)/2048)) & ((y < -sqrt(10720697935)/51200) | (y < sqrt(17157311)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10720697935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17157311), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10720697935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10720697935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17157311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17157311), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10720697935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17157311), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(y:sympy.Rational):
	#((y > sqrt(2664819015)/25600) | (y > -sqrt(4264759)/1024)) & ((y > sqrt(2664819015)/25600) | (y < -sqrt(2664819015)/25600)) & ((y > -sqrt(4264759)/1024) | (y < sqrt(4264759)/1024)) & ((y < -sqrt(2664819015)/25600) | (y < sqrt(4264759)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2664819015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4264759), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2664819015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2664819015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4264759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4264759), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2664819015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4264759), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(y:sympy.Rational):
	#((y > 3*sqrt(304854335)/25600) | (y > -sqrt(4390951)/1024)) & ((y > 3*sqrt(304854335)/25600) | (y < -3*sqrt(304854335)/25600)) & ((y > -sqrt(4390951)/1024) | (y < sqrt(4390951)/1024)) & ((y < -3*sqrt(304854335)/25600) | (y < sqrt(4390951)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(304854335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4390951), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(304854335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(304854335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4390951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4390951), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(304854335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4390951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(y:sympy.Rational):
	#((y > -sqrt(1085095)/512) | (y > 3*sqrt(75335615)/12800)) & ((y > -sqrt(1085095)/512) | (y < sqrt(1085095)/512)) & ((y > 3*sqrt(75335615)/12800) | (y < -3*sqrt(75335615)/12800)) & ((y < sqrt(1085095)/512) | (y < -3*sqrt(75335615)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1085095), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(75335615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1085095), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1085095), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(75335615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(75335615), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1085095), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(75335615), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(y:sympy.Rational):
	#((y > sqrt(2725069015)/25600) | (y > -sqrt(4361159)/1024)) & ((y > sqrt(2725069015)/25600) | (y < -sqrt(2725069015)/25600)) & ((y > -sqrt(4361159)/1024) | (y < sqrt(4361159)/1024)) & ((y < -sqrt(2725069015)/25600) | (y < sqrt(4361159)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2725069015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4361159), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2725069015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2725069015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4361159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4361159), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2725069015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4361159), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(y:sympy.Rational):
	#((y > sqrt(10972447935)/51200) | (y > -sqrt(17560111)/2048)) & ((y > sqrt(10972447935)/51200) | (y < -sqrt(10972447935)/51200)) & ((y > -sqrt(17560111)/2048) | (y < sqrt(17560111)/2048)) & ((y < -sqrt(10972447935)/51200) | (y < sqrt(17560111)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10972447935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17560111), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10972447935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10972447935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17560111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17560111), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10972447935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17560111), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(y:sympy.Rational):
	#((y > -sqrt(1098199)/512) | (y > 9*sqrt(8471735)/12800)) & ((y > -sqrt(1098199)/512) | (y < sqrt(1098199)/512)) & ((y > 9*sqrt(8471735)/12800) | (y < -9*sqrt(8471735)/12800)) & ((y < sqrt(1098199)/512) | (y < -9*sqrt(8471735)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1098199), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(9, 12800), Pow(Integer(8471735), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1098199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1098199), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(9, 12800), Pow(Integer(8471735), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 12800), Pow(Integer(8471735), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1098199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 12800), Pow(Integer(8471735), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(y:sympy.Rational):
	#((y > sqrt(166628415)/6400) | (y > -sqrt(266671)/256)) & ((y > sqrt(166628415)/6400) | (y < -sqrt(166628415)/6400)) & ((y > -sqrt(266671)/256) | (y < sqrt(266671)/256)) & ((y < -sqrt(166628415)/6400) | (y < sqrt(266671)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(166628415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(266671), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(166628415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(166628415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(266671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(266671), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(166628415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(266671), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(y:sympy.Rational):
	#((y > sqrt(10930687935)/51200) | (y > -sqrt(17493295)/2048)) & ((y > sqrt(10930687935)/51200) | (y < -sqrt(10930687935)/51200)) & ((y > -sqrt(17493295)/2048) | (y < sqrt(17493295)/2048)) & ((y < -sqrt(10930687935)/51200) | (y < sqrt(17493295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10930687935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17493295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10930687935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10930687935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17493295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17493295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10930687935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17493295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(y:sympy.Rational):
	#((y > 3*sqrt(4671015)/3200) | (y > -sqrt(67279)/128)) & ((y > 3*sqrt(4671015)/3200) | (y < -3*sqrt(4671015)/3200)) & ((y > -sqrt(67279)/128) | (y < sqrt(67279)/128)) & ((y < -3*sqrt(4671015)/3200) | (y < sqrt(67279)/128))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 3200), Pow(Integer(4671015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67279), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 3200), Pow(Integer(4671015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 3200), Pow(Integer(4671015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67279), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 3200), Pow(Integer(4671015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(y:sympy.Rational):
	#((y > sqrt(167853415)/6400) | (y > -sqrt(268631)/256)) & ((y > sqrt(167853415)/6400) | (y < -sqrt(167853415)/6400)) & ((y > -sqrt(268631)/256) | (y < sqrt(268631)/256)) & ((y < -sqrt(167853415)/6400) | (y < sqrt(268631)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(167853415), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(268631), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 6400), Pow(Integer(167853415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(167853415), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(268631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(268631), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 6400), Pow(Integer(167853415), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(268631), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(y:sympy.Rational):
	#((y > 3*sqrt(1208264215)/51200) | (y > -sqrt(17403199)/2048)) & ((y > 3*sqrt(1208264215)/51200) | (y < -3*sqrt(1208264215)/51200)) & ((y > -sqrt(17403199)/2048) | (y < sqrt(17403199)/2048)) & ((y < -3*sqrt(1208264215)/51200) | (y < sqrt(17403199)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1208264215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17403199), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1208264215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1208264215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17403199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17403199), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1208264215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17403199), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(y:sympy.Rational):
	#((y > sqrt(10921352935)/51200) | (y > -sqrt(17478359)/2048)) & ((y > sqrt(10921352935)/51200) | (y < -sqrt(10921352935)/51200)) & ((y > -sqrt(17478359)/2048) | (y < sqrt(17478359)/2048)) & ((y < -sqrt(10921352935)/51200) | (y < sqrt(17478359)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10921352935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17478359), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10921352935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10921352935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17478359), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17478359), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10921352935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17478359), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(y:sympy.Rational):
	#((y > 3*sqrt(300149335)/25600) | (y > -sqrt(4323199)/1024)) & ((y > 3*sqrt(300149335)/25600) | (y < -3*sqrt(300149335)/25600)) & ((y > -sqrt(4323199)/1024) | (y < sqrt(4323199)/1024)) & ((y < -3*sqrt(300149335)/25600) | (y < sqrt(4323199)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(300149335), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4323199), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 25600), Pow(Integer(300149335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(300149335), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4323199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4323199), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 25600), Pow(Integer(300149335), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4323199), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(y:sympy.Rational):
	#((y > sqrt(2689294015)/25600) | (y > -sqrt(4303919)/1024)) & ((y > sqrt(2689294015)/25600) | (y < -sqrt(2689294015)/25600)) & ((y > -sqrt(4303919)/1024) | (y < sqrt(4303919)/1024)) & ((y < -sqrt(2689294015)/25600) | (y < sqrt(4303919)/1024))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2689294015), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4303919), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 25600), Pow(Integer(2689294015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2689294015), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1024), Pow(Integer(4303919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4303919), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 25600), Pow(Integer(2689294015), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 1024), Pow(Integer(4303919), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(y:sympy.Rational):
	#((y > 3*sqrt(1212444215)/51200) | (y > -sqrt(17463391)/2048)) & ((y > 3*sqrt(1212444215)/51200) | (y < -3*sqrt(1212444215)/51200)) & ((y > -sqrt(17463391)/2048) | (y < sqrt(17463391)/2048)) & ((y < -3*sqrt(1212444215)/51200) | (y < sqrt(17463391)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1212444215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17463391), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1212444215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1212444215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17463391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17463391), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1212444215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17463391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(y:sympy.Rational):
	#((y > sqrt(10817347935)/51200) | (y > -sqrt(17311951)/2048)) & ((y > sqrt(10817347935)/51200) | (y < -sqrt(10817347935)/51200)) & ((y > -sqrt(17311951)/2048) | (y < sqrt(17311951)/2048)) & ((y < -sqrt(10817347935)/51200) | (y < sqrt(17311951)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10817347935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17311951), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10817347935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10817347935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17311951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17311951), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10817347935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17311951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(y:sympy.Rational):
	#((y > -sqrt(1083191)/512) | (y > sqrt(676830535)/12800)) & ((y > -sqrt(1083191)/512) | (y < sqrt(1083191)/512)) & ((y > sqrt(676830535)/12800) | (y < -sqrt(676830535)/12800)) & ((y < sqrt(1083191)/512) | (y < -sqrt(676830535)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1083191), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(676830535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(1083191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1083191), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(676830535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(676830535), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(1083191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(676830535), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(y:sympy.Rational):
	#((y > sqrt(680385535)/12800) | (y > -11*sqrt(8999)/512)) & ((y > sqrt(680385535)/12800) | (y < -sqrt(680385535)/12800)) & ((y > -11*sqrt(8999)/512) | (y < 11*sqrt(8999)/512)) & ((y < -sqrt(680385535)/12800) | (y < 11*sqrt(8999)/512))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(680385535), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 512), Pow(Integer(8999), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 12800), Pow(Integer(680385535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(680385535), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 512), Pow(Integer(8999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 512), Pow(Integer(8999), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 12800), Pow(Integer(680385535), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(11, 512), Pow(Integer(8999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(y:sympy.Rational):
	#((y > 3*sqrt(1198194215)/51200) | (y > -sqrt(17258191)/2048)) & ((y > 3*sqrt(1198194215)/51200) | (y < -3*sqrt(1198194215)/51200)) & ((y > -sqrt(17258191)/2048) | (y < sqrt(17258191)/2048)) & ((y < -3*sqrt(1198194215)/51200) | (y < sqrt(17258191)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1198194215), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17258191), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 51200), Pow(Integer(1198194215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1198194215), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17258191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17258191), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 51200), Pow(Integer(1198194215), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17258191), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(y:sympy.Rational):
	#((y > -31*sqrt(1111)/512) | (y > 3*sqrt(74125615)/12800)) & ((y > -31*sqrt(1111)/512) | (y < 31*sqrt(1111)/512)) & ((y > 3*sqrt(74125615)/12800) | (y < -3*sqrt(74125615)/12800)) & ((y < 31*sqrt(1111)/512) | (y < -3*sqrt(74125615)/12800))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(31, 512), Pow(Integer(1111), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(74125615), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(31, 512), Pow(Integer(1111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(31, 512), Pow(Integer(1111), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 12800), Pow(Integer(74125615), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(74125615), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Rational(31, 512), Pow(Integer(1111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 12800), Pow(Integer(74125615), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(y:sympy.Rational):
	#((y > sqrt(10671622935)/51200) | (y > -sqrt(17078791)/2048)) & ((y > sqrt(10671622935)/51200) | (y < -sqrt(10671622935)/51200)) & ((y > -sqrt(17078791)/2048) | (y < sqrt(17078791)/2048)) & ((y < -sqrt(10671622935)/51200) | (y < sqrt(17078791)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10671622935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17078791), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10671622935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10671622935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17078791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17078791), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10671622935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17078791), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(y:sympy.Rational):
	#((y > sqrt(10883812935)/51200) | (y > -sqrt(17418295)/2048)) & ((y > sqrt(10883812935)/51200) | (y < -sqrt(10883812935)/51200)) & ((y > -sqrt(17418295)/2048) | (y < sqrt(17418295)/2048)) & ((y < -sqrt(10883812935)/51200) | (y < sqrt(17418295)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10883812935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17418295), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10883812935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10883812935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17418295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17418295), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10883812935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17418295), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(y:sympy.Rational):
	#((y > 3*sqrt(18915935)/6400) | (y > -sqrt(272455)/256)) & ((y > 3*sqrt(18915935)/6400) | (y < -3*sqrt(18915935)/6400)) & ((y > -sqrt(272455)/256) | (y < sqrt(272455)/256)) & ((y < -3*sqrt(18915935)/6400) | (y < sqrt(272455)/256))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18915935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(272455), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(3, 6400), Pow(Integer(18915935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18915935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(272455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(272455), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 6400), Pow(Integer(18915935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(272455), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(y:sympy.Rational):
	#((y > sqrt(10822127935)/51200) | (y > -sqrt(17319599)/2048)) & ((y > sqrt(10822127935)/51200) | (y < -sqrt(10822127935)/51200)) & ((y > -sqrt(17319599)/2048) | (y < sqrt(17319599)/2048)) & ((y < -sqrt(10822127935)/51200) | (y < sqrt(17319599)/2048))

	pre_cond = And(Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10822127935), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17319599), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Rational(1, 51200), Pow(Integer(10822127935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10822127935), Rational(1, 2))))), Or(StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2048), Pow(Integer(17319599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17319599), Rational(1, 2))))), Or(StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 51200), Pow(Integer(10822127935), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Rational(1, 2048), Pow(Integer(17319599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(y:sympy.Rational, x:sympy.Rational):
	# (0 > x**2 + y**2 - 5) & (0 > -x**2 - y**2 + 4999/1000)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-5))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(4999, 1000))))

	eval = post_cond.subs( { 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of y:\n"))
	ip_1=int(input("enter integer denominator of y:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	y=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(y=y)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 1143/512')
		exit(0)
	
	
	if pre_condition_1(y=y)==True:
		print("pre_condition_1 SAT")
		print('x = 1143/512')
		print('y = 1/8')
		exit(0)
	
	
	if pre_condition_2(y=y)==True:
		print("pre_condition_2 SAT")
		print('x = 2047/2048')
		print('y = 2')
		exit(0)
	
	
	if pre_condition_3(y=y)==True:
		print("pre_condition_3 SAT")
		print('x = 89/128')
		print('y = 17/8')
		exit(0)
	
	
	if pre_condition_4(y=y)==True:
		print("pre_condition_4 SAT")
		print('x = 8191/4096')
		print('y = -1')
		exit(0)
	
	
	if pre_condition_5(y=y)==True:
		print("pre_condition_5 SAT")
		print('x = 9155/4096')
		print('y = 1/16')
		exit(0)
	
	
	if pre_condition_6(y=y)==True:
		print("pre_condition_6 SAT")
		print('x = 221/256')
		print('y = 33/16')
		exit(0)
	
	
	if pre_condition_7(y=y)==True:
		print("pre_condition_7 SAT")
		print('x = 957/1024')
		print('y = 65/32')
		exit(0)
	
	
	if pre_condition_8(y=y)==True:
		print("pre_condition_8 SAT")
		print('x = 18317/8192')
		print('y = 0')
		exit(0)
	
	
	if pre_condition_9(y=y)==True:
		print("pre_condition_9 SAT")
		print('x = 991/1024')
		print('y = 129/64')
		exit(0)
	
	
	if pre_condition_10(y=y)==True:
		print("pre_condition_10 SAT")
		print('x = 4575/2048')
		print('y = 3/32')
		exit(0)
	
	
	if pre_condition_11(y=y)==True:
		print("pre_condition_11 SAT")
		print('x = 18295/8192')
		print('y = 7/64')
		exit(0)
	
	
	if pre_condition_12(y=y)==True:
		print("pre_condition_12 SAT")
		print('x = 2015/2048')
		print('y = 257/128')
		exit(0)
	
	
	if pre_condition_13(y=y)==True:
		print("pre_condition_13 SAT")
		print('x = 1999/2048')
		print('y = -515/256')
		exit(0)
	
	
	if pre_condition_14(y=y)==True:
		print("pre_condition_14 SAT")
		print('x = 2031/2048')
		print('y = 513/256')
		exit(0)
	
	
	if pre_condition_15(y=y)==True:
		print("pre_condition_15 SAT")
		print('x = 2007/2048')
		print('y = 1029/512')
		exit(0)
	
	
	if pre_condition_16(y=y)==True:
		print("pre_condition_16 SAT")
		print('x = 2023/2048')
		print('y = 1027/512')
		exit(0)
	
	
	if pre_condition_17(y=y)==True:
		print("pre_condition_17 SAT")
		print('x = 995/1024')
		print('y = -1031/512')
		exit(0)
	
	
	if pre_condition_18(y=y)==True:
		print("pre_condition_18 SAT")
		print('x = 1843/2048')
		print('y = -131/64')
		exit(0)
	
	
	if pre_condition_19(y=y)==True:
		print("pre_condition_19 SAT")
		print('x = 1879/2048')
		print('y = 261/128')
		exit(0)
	
	
	if pre_condition_20(y=y)==True:
		print("pre_condition_20 SAT")
		print('x = 903/1024')
		print('y = -263/128')
		exit(0)
	
	
	if pre_condition_21(y=y)==True:
		print("pre_condition_21 SAT")
		print('x = 2011/2048')
		print('y = 2057/1024')
		exit(0)
	
	
	if pre_condition_22(y=y)==True:
		print("pre_condition_22 SAT")
		print('x = 2013/2048')
		print('y = -4113/2048')
		exit(0)
	
	
	if pre_condition_23(y=y)==True:
		print("pre_condition_23 SAT")
		print('x = 1787/2048')
		print('y = 527/256')
		exit(0)
	
	
	if pre_condition_24(y=y)==True:
		print("pre_condition_24 SAT")
		print('x = 889/1024')
		print('y = -1055/512')
		exit(0)
	
	
	if pre_condition_25(y=y)==True:
		print("pre_condition_25 SAT")
		print('x = 1825/2048')
		print('y = 525/256')
		exit(0)
	
	
	if pre_condition_26(y=y)==True:
		print("pre_condition_26 SAT")
		print('x = 1897/2048')
		print('y = -521/256')
		exit(0)
	
	
	if pre_condition_27(y=y)==True:
		print("pre_condition_27 SAT")
		print('x = 2039/2048')
		print('y = 1025/512')
		exit(0)
	
	
	if pre_condition_28(y=y)==True:
		print("pre_condition_28 SAT")
		print('x = 1773/2048')
		print('y = -2111/1024')
		exit(0)
	
	
	if pre_condition_29(y=y)==True:
		print("pre_condition_29 SAT")
		print('x = 503/512')
		print('y = 8227/4096')
		exit(0)
	
	
	if pre_condition_30(y=y)==True:
		print("pre_condition_30 SAT")
		print('x = 1905/2048')
		print('y = 1041/512')
		exit(0)
	
	
	if pre_condition_31(y=y)==True:
		print("pre_condition_31 SAT")
		print('x = 443/512')
		print('y = -8445/4096')
		exit(0)
	
	
	if pre_condition_32(y=y)==True:
		print("pre_condition_32 SAT")
		print('x = 59/64')
		print('y = 1043/512')
		exit(0)
	
	
	if pre_condition_33(y=y)==True:
		print("pre_condition_33 SAT")
		print('x = 2003/2048')
		print('y = 2059/1024')
		exit(0)
	
	
	if pre_condition_34(y=y)==True:
		print("pre_condition_34 SAT")
		print('x = 1883/2048')
		print('y = 2087/1024')
		exit(0)
	
	
	if pre_condition_35(y=y)==True:
		print("pre_condition_35 SAT")
		print('x = 1861/2048')
		print('y = -523/256')
		exit(0)
	
	
	if pre_condition_36(y=y)==True:
		print("pre_condition_36 SAT")
		print('x = 1007/1024')
		print('y = 8225/4096')
		exit(0)
	
	
	if pre_condition_37(y=y)==True:
		print("pre_condition_37 SAT")
		print('x = 955/1024')
		print('y = 2081/1024')
		exit(0)
	
	
	if pre_condition_38(y=y)==True:
		print("pre_condition_38 SAT")
		print('x = 935/1024')
		print('y = 1045/512')
		exit(0)
	
	
	if pre_condition_39(y=y)==True:
		print("pre_condition_39 SAT")
		print('x = 111/128')
		print('y = -4221/2048')
		exit(0)
	
	
	if pre_condition_40(y=y)==True:
		print("pre_condition_40 SAT")
		print('x = 4573/2048')
		print('y = 15/128')
		exit(0)
	
	
	if pre_condition_41(y=y)==True:
		print("pre_condition_41 SAT")
		print('x = 473/512')
		print('y = -2085/1024')
		exit(0)
	
	
	if pre_condition_42(y=y)==True:
		print("pre_condition_42 SAT")
		print('x = 945/1024')
		print('y = 4171/2048')
		exit(0)
	
	
	if pre_condition_43(y=y)==True:
		print("pre_condition_43 SAT")
		print('x = 1771/2048')
		print('y = -16891/8192')
		exit(0)
	
	
	if pre_condition_44(y=y)==True:
		print("pre_condition_44 SAT")
		print('x = 2009/2048')
		print('y = 4115/2048')
		exit(0)
	
	
	if pre_condition_45(y=y)==True:
		print("pre_condition_45 SAT")
		print('x = 2043/2048')
		print('y = 2049/1024')
		exit(0)
	
	
	if pre_condition_46(y=y)==True:
		print("pre_condition_46 SAT")
		print('x = 1783/2048')
		print('y = 2109/1024')
		exit(0)
	
	
	if pre_condition_47(y=y)==True:
		print("pre_condition_47 SAT")
		print('x = 937/1024')
		print('y = 2089/1024')
		exit(0)
	
	
	if pre_condition_48(y=y)==True:
		print("pre_condition_48 SAT")
		print('x = 917/1024')
		print('y = -1049/512')
		exit(0)
	
	
	if pre_condition_49(y=y)==True:
		print("pre_condition_49 SAT")
		print('x = 251/256')
		print('y = 8231/4096')
		exit(0)
	
	
	if pre_condition_50(y=y)==True:
		print("pre_condition_50 SAT")
		print('x = 2041/2048')
		print('y = -4099/2048')
		exit(0)
	
	
	if pre_condition_51(y=y)==True:
		print("pre_condition_51 SAT")
		print('x = 9145/4096')
		print('y = 31/256')
		exit(0)
	
	
	if pre_condition_52(y=y)==True:
		print("pre_condition_52 SAT")
		print('x = 887/1024')
		print('y = -8443/4096')
		exit(0)
	
	
	if pre_condition_53(y=y)==True:
		print("pre_condition_53 SAT")
		print('x = 919/1024')
		print('y = 2097/1024')
		exit(0)
	
	
	if pre_condition_54(y=y)==True:
		print("pre_condition_54 SAT")
		print('x = 255/256')
		print('y = 8199/4096')
		exit(0)
	
	
	if pre_condition_55(y=y)==True:
		print("pre_condition_55 SAT")
		print('x = 933/1024')
		print('y = 2091/1024')
		exit(0)
	
	
	if pre_condition_56(y=y)==True:
		print("pre_condition_56 SAT")
		print('x = 18289/8192')
		print('y = 253/2048')
		exit(0)
	
	
	if pre_condition_57(y=y)==True:
		print("pre_condition_57 SAT")
		print('x = 18291/8192')
		print('y = 61/512')
		exit(0)
	
	
	if pre_condition_58(y=y)==True:
		print("pre_condition_58 SAT")
		print('x = 227/256')
		print('y = -1051/512')
		exit(0)
	
	
	if pre_condition_59(y=y)==True:
		print("pre_condition_59 SAT")
		print('x = 9147/4096')
		print('y = 29/256')
		exit(0)
	
	
	if pre_condition_60(y=y)==True:
		print("pre_condition_60 SAT")
		print('x = 463/512')
		print('y = -1047/512')
		exit(0)
	
	
	if pre_condition_61(y=y)==True:
		print("pre_condition_61 SAT")
		print('x = 1775/2048')
		print('y = -16885/8192')
		exit(0)
	
	
	if pre_condition_62(y=y)==True:
		print("pre_condition_62 SAT")
		print('x = 1777/2048')
		print('y = -8441/4096')
		exit(0)
	
	
	if pre_condition_63(y=y)==True:
		print("pre_condition_63 SAT")
		print('x = 1863/2048')
		print('y = -4183/2048')
		exit(0)
	
	
	if pre_condition_64(y=y)==True:
		print("pre_condition_64 SAT")
		print('x = 2005/2048')
		print('y = -4117/2048')
		exit(0)
	
	
	if pre_condition_65(y=y)==True:
		print("pre_condition_65 SAT")
		print('x = 29/32')
		print('y = -2093/1024')
		exit(0)
	
	
	if pre_condition_66(y=y)==True:
		print("pre_condition_66 SAT")
		print('x = 455/512')
		print('y = -2101/1024')
		exit(0)
	
	
	if pre_condition_67(y=y)==True:
		print("pre_condition_67 SAT")
		print('x = 2019/2048')
		print('y = -2055/1024')
		exit(0)
	
	
	if pre_condition_68(y=y)==True:
		print("pre_condition_68 SAT")
		print('x = 911/1024')
		print('y = 4201/2048')
		exit(0)
	
	
	if pre_condition_69(y=y)==True:
		print("pre_condition_69 SAT")
		print('x = 2027/2048')
		print('y = 2053/1024')
		exit(0)
	
	
	if pre_condition_70(y=y)==True:
		print("pre_condition_70 SAT")
		print('x = 1797/2048')
		print('y = -1053/512')
		exit(0)
	
	
	if pre_condition_71(y=y)==True:
		print("pre_condition_71 SAT")
		print('x = 18293/8192')
		print('y = 117/1024')
		exit(0)
	
	
	if pre_condition_72(y=y)==True:
		print("pre_condition_72 SAT")
		print('x = 1005/1024')
		print('y = 8229/4096')
		exit(0)
	
	
	if pre_condition_73(y=y)==True:
		print("pre_condition_73 SAT")
		print('x = 2001/2048')
		print('y = -4119/2048')
		exit(0)
	
	
	if pre_condition_74(y=y)==True:
		print("pre_condition_74 SAT")
		print('x = 931/1024')
		print('y = -8367/4096')
		exit(0)
	
	
	if pre_condition_75(y=y)==True:
		print("pre_condition_75 SAT")
		print('x = 459/512')
		print('y = -4195/2048')
		exit(0)
	
	
	if pre_condition_76(y=y)==True:
		print("pre_condition_76 SAT")
		print('x = 947/1024')
		print('y = 4169/2048')
		exit(0)
	
	
	if pre_condition_77(y=y)==True:
		print("pre_condition_77 SAT")
		print('x = 927/1024')
		print('y = 4187/2048')
		exit(0)
	
	
	if pre_condition_78(y=y)==True:
		print("pre_condition_78 SAT")
		print('x = 909/1024')
		print('y = -4203/2048')
		exit(0)
	
	
	if pre_condition_79(y=y)==True:
		print("pre_condition_79 SAT")
		print('x = 1003/1024')
		print('y = 8233/4096')
		exit(0)
	
	
	if pre_condition_80(y=y)==True:
		print("pre_condition_80 SAT")
		print('x = 1891/2048')
		print('y = -8341/4096')
		exit(0)
	
	
	if pre_condition_81(y=y)==True:
		print("pre_condition_81 SAT")
		print('x = 125/128')
		print('y = -8239/4096')
		exit(0)
	
	
	if pre_condition_82(y=y)==True:
		print("pre_condition_82 SAT")
		print('x = 9149/4096')
		print('y = 13/128')
		exit(0)
	
	
	if pre_condition_83(y=y)==True:
		print("pre_condition_83 SAT")
		print('x = 1859/2048')
		print('y = -4185/2048')
		exit(0)
	
	
	if pre_condition_84(y=y)==True:
		print("pre_condition_84 SAT")
		print('x = 18299/8192')
		print('y = 203/2048')
		exit(0)
	
	
	if pre_condition_85(y=y)==True:
		print("pre_condition_85 SAT")
		print('x = 2045/2048')
		print('y = 4097/2048')
		exit(0)
	
	
	if pre_condition_86(y=y)==True:
		print("pre_condition_86 SAT")
		print('x = 7/8')
		print('y = -2107/1024')
		exit(0)
	
	
	if pre_condition_87(y=y)==True:
		print("pre_condition_87 SAT")
		print('x = 2021/2048')
		print('y = -4109/2048')
		exit(0)
	
	
	if pre_condition_88(y=y)==True:
		print("pre_condition_88 SAT")
		print('x = 2287/1024')
		print('y = 27/256')
		exit(0)
	
	
	if pre_condition_89(y=y)==True:
		print("pre_condition_89 SAT")
		print('x = 1829/2048')
		print('y = 2099/1024')
		exit(0)
	
	
	if pre_condition_90(y=y)==True:
		print("pre_condition_90 SAT")
		print('x = 511/512')
		print('y = 8195/4096')
		exit(0)
	
	
	if pre_condition_91(y=y)==True:
		print("pre_condition_91 SAT")
		print('x = 18297/8192')
		print('y = 107/1024')
		exit(0)
	
	
	if pre_condition_92(y=y)==True:
		print("pre_condition_92 SAT")
		print('x = 993/1024')
		print('y = -2063/1024')
		exit(0)
	
	
	if pre_condition_93(y=y)==True:
		print("pre_condition_93 SAT")
		print('x = 2035/2048')
		print('y = 2051/1024')
		exit(0)
	
	
	if pre_condition_94(y=y)==True:
		print("pre_condition_94 SAT")
		print('x = 31/32')
		print('y = -4127/2048')
		exit(0)
	
	
	if pre_condition_95(y=y)==True:
		print("pre_condition_95 SAT")
		print('x = 929/1024')
		print('y = -8371/4096')
		exit(0)
	
	
	if pre_condition_96(y=y)==True:
		print("pre_condition_96 SAT")
		print('x = 1785/2048')
		print('y = -4217/2048')
		exit(0)
	
	
	if pre_condition_97(y=y)==True:
		print("pre_condition_97 SAT")
		print('x = 465/512')
		print('y = 8369/4096')
		exit(0)
	
	
	if pre_condition_98(y=y)==True:
		print("pre_condition_98 SAT")
		print('x = 1817/2048')
		print('y = -67251/32768')
		exit(0)
	
	
	if pre_condition_99(y=y)==True:
		print("pre_condition_99 SAT")
		print('x = 223/256')
		print('y = -8435/4096')
		exit(0)
	
	
	if pre_condition_100(y=y)==True:
		print("pre_condition_100 SAT")
		print('x = 893/1024')
		print('y = -8433/4096')
		exit(0)
	
	
	if pre_condition_101(y=y)==True:
		print("pre_condition_101 SAT")
		print('x = 1011/1024')
		print('y = 8217/4096')
		exit(0)
	
	
	if pre_condition_102(y=y)==True:
		print("pre_condition_102 SAT")
		print('x = 445/512')
		print('y = -4219/2048')
		exit(0)
	
	
	if pre_condition_103(y=y)==True:
		print("pre_condition_103 SAT")
		print('x = 897/1024')
		print('y = -4213/2048')
		exit(0)
	
	
	if pre_condition_104(y=y)==True:
		print("pre_condition_104 SAT")
		print('x = 1827/2048')
		print('y = 4199/2048')
		exit(0)
	
	
	if pre_condition_105(y=y)==True:
		print("pre_condition_105 SAT")
		print('x = 117/128')
		print('y = -4179/2048')
		exit(0)
	
	
	if pre_condition_106(y=y)==True:
		print("pre_condition_106 SAT")
		print('x = 895/1024')
		print('y = -4215/2048')
		exit(0)
	
	
	if pre_condition_107(y=y)==True:
		print("pre_condition_107 SAT")
		print('x = 9153/4096')
		print('y = 5/64')
		exit(0)
	
	
	if pre_condition_108(y=y)==True:
		print("pre_condition_108 SAT")
		print('x = 237/256')
		print('y = 8337/4096')
		exit(0)
	
	
	if pre_condition_109(y=y)==True:
		print("pre_condition_109 SAT")
		print('x = 1819/2048')
		print('y = -8405/4096')
		exit(0)
	
	
	if pre_condition_110(y=y)==True:
		print("pre_condition_110 SAT")
		print('x = 1001/1024')
		print('y = -8237/4096')
		exit(0)
	
	
	if pre_condition_111(y=y)==True:
		print("pre_condition_111 SAT")
		print('x = 1779/2048')
		print('y = -8439/4096')
		exit(0)
	
	
	if pre_condition_112(y=y)==True:
		print("pre_condition_112 SAT")
		print('x = 891/1024')
		print('y = -8437/4096')
		exit(0)
	
	
	if pre_condition_113(y=y)==True:
		print("pre_condition_113 SAT")
		print('x = 1985/2048')
		print('y = 8253/4096')
		exit(0)
	
	
	if pre_condition_114(y=y)==True:
		print("pre_condition_114 SAT")
		print('x = 1901/2048')
		print('y = 2083/1024')
		exit(0)
	
	
	if pre_condition_115(y=y)==True:
		print("pre_condition_115 SAT")
		print('x = 1853/2048')
		print('y = -66999/32768')
		exit(0)
	
	
	if pre_condition_116(y=y)==True:
		print("pre_condition_116 SAT")
		print('x = 501/512')
		print('y = 8235/4096')
		exit(0)
	
	
	if pre_condition_117(y=y)==True:
		print("pre_condition_117 SAT")
		print('x = 1023/1024')
		print('y = 8193/4096')
		exit(0)
	
	
	if pre_condition_118(y=y)==True:
		print("pre_condition_118 SAT")
		print('x = 1835/2048')
		print('y = 8391/4096')
		exit(0)
	
	
	if pre_condition_119(y=y)==True:
		print("pre_condition_119 SAT")
		print('x = 143/64')
		print('y = 11/128')
		exit(0)
	
	
	if pre_condition_120(y=y)==True:
		print("pre_condition_120 SAT")
		print('x = 1983/2048')
		print('y = -8255/4096')
		exit(0)
	
	
	if pre_condition_121(y=y)==True:
		print("pre_condition_121 SAT")
		print('x = 57/64')
		print('y = -8401/4096')
		exit(0)
	
	
	if pre_condition_122(y=y)==True:
		print("pre_condition_122 SAT")
		print('x = 239/256')
		print('y = -4161/2048')
		exit(0)
	
	
	if pre_condition_123(y=y)==True:
		print("pre_condition_123 SAT")
		print('x = 2033/2048')
		print('y = 4103/2048')
		exit(0)
	
	
	if pre_condition_124(y=y)==True:
		print("pre_condition_124 SAT")
		print('x = 497/512')
		print('y = -4125/2048')
		exit(0)
	
	
	if pre_condition_125(y=y)==True:
		print("pre_condition_125 SAT")
		print('x = 2029/2048')
		print('y = 4105/2048')
		exit(0)
	
	
	if pre_condition_126(y=y)==True:
		print("pre_condition_126 SAT")
		print('x = 1791/2048')
		print('y = -8429/4096')
		exit(0)
	
	
	if pre_condition_127(y=y)==True:
		print("pre_condition_127 SAT")
		print('x = 1793/2048')
		print('y = 8427/4096')
		exit(0)
	
	
	if pre_condition_128(y=y)==True:
		print("pre_condition_128 SAT")
		print('x = 18305/8192')
		print('y = 165/2048')
		exit(0)
	
	
	if pre_condition_129(y=y)==True:
		print("pre_condition_129 SAT")
		print('x = 457/512')
		print('y = -8397/4096')
		exit(0)
	
	
	if pre_condition_130(y=y)==True:
		print("pre_condition_130 SAT")
		print('x = 447/512')
		print('y = -8431/4096')
		exit(0)
	
	
	if pre_condition_131(y=y)==True:
		print("pre_condition_131 SAT")
		print('x = 1781/2048')
		print('y = -16875/8192')
		exit(0)
	
	
	if pre_condition_132(y=y)==True:
		print("pre_condition_132 SAT")
		print('x = 1855/2048')
		print('y = -16747/8192')
		exit(0)
	
	
	if pre_condition_133(y=y)==True:
		print("pre_condition_133 SAT")
		print('x = 1821/2048')
		print('y = -8403/4096')
		exit(0)
	
	
	if pre_condition_134(y=y)==True:
		print("pre_condition_134 SAT")
		print('x = 9151/4096')
		print('y = 23/256')
		exit(0)
	
	
	if pre_condition_135(y=y)==True:
		print("pre_condition_135 SAT")
		print('x = 901/1024')
		print('y = -2105/1024')
		exit(0)
	
	
	if pre_condition_136(y=y)==True:
		print("pre_condition_136 SAT")
		print('x = 1789/2048')
		print('y = -16861/8192')
		exit(0)
	
	
	if pre_condition_137(y=y)==True:
		print("pre_condition_137 SAT")
		print('x = 1857/2048')
		print('y = -16743/8192')
		exit(0)
	
	
	if pre_condition_138(y=y)==True:
		print("pre_condition_138 SAT")
		print('x = 1899/2048')
		print('y = -4167/2048')
		exit(0)
	
	
	if pre_condition_139(y=y)==True:
		print("pre_condition_139 SAT")
		print('x = 449/512')
		print('y = -8425/4096')
		exit(0)
	
	
	if pre_condition_140(y=y)==True:
		print("pre_condition_140 SAT")
		print('x = 467/512')
		print('y = 4181/2048')
		exit(0)
	
	
	if pre_condition_141(y=y)==True:
		print("pre_condition_141 SAT")
		print('x = 1987/2048')
		print('y = 8251/4096')
		exit(0)
	
	
	if pre_condition_142(y=y)==True:
		print("pre_condition_142 SAT")
		print('x = 18301/8192')
		print('y = 191/2048')
		exit(0)
	
	
	if pre_condition_143(y=y)==True:
		print("pre_condition_143 SAT")
		print('x = 1795/2048')
		print('y = -16851/8192')
		exit(0)
	
	
	if pre_condition_144(y=y)==True:
		print("pre_condition_144 SAT")
		print('x = 1799/2048')
		print('y = -4211/2048')
		exit(0)
	
	
	if pre_condition_145(y=y)==True:
		print("pre_condition_145 SAT")
		print('x = 943/1024')
		print('y = 4173/2048')
		exit(0)
	
	
	if pre_condition_146(y=y)==True:
		print("pre_condition_146 SAT")
		print('x = 2017/2048')
		print('y = -4111/2048')
		exit(0)
	
	
	if pre_condition_147(y=y)==True:
		print("pre_condition_147 SAT")
		print('x = 1995/2048')
		print('y = -2061/1024')
		exit(0)
	
	
	if pre_condition_148(y=y)==True:
		print("pre_condition_148 SAT")
		print('x = 231/256')
		print('y = 2095/1024')
		exit(0)
	
	
	if pre_condition_149(y=y)==True:
		print("pre_condition_149 SAT")
		print('x = 1801/2048')
		print('y = -67361/32768')
		exit(0)
	
	
	if pre_condition_150(y=y)==True:
		print("pre_condition_150 SAT")
		print('x = 925/1024')
		print('y = 4189/2048')
		exit(0)
	
	
	if pre_condition_151(y=y)==True:
		print("pre_condition_151 SAT")
		print('x = 1903/2048')
		print('y = -4165/2048')
		exit(0)
	
	
	if pre_condition_152(y=y)==True:
		print("pre_condition_152 SAT")
		print('x = 18303/8192')
		print('y = 179/2048')
		exit(0)
	
	
	if pre_condition_153(y=y)==True:
		print("pre_condition_153 SAT")
		print('x = 2025/2048')
		print('y = 4107/2048')
		exit(0)
	
	
	if pre_condition_154(y=y)==True:
		print("pre_condition_154 SAT")
		print('x = 1021/1024')
		print('y = 8197/4096')
		exit(0)
	
	
	if pre_condition_155(y=y)==True:
		print("pre_condition_155 SAT")
		print('x = 4577/2048')
		print('y = 9/128')
		exit(0)
	
	
	if pre_condition_156(y=y)==True:
		print("pre_condition_156 SAT")
		print('x = 1877/2048')
		print('y = 4177/2048')
		exit(0)
	
	
	if pre_condition_157(y=y)==True:
		print("pre_condition_157 SAT")
		print('x = 1881/2048')
		print('y = -4175/2048')
		exit(0)
	
	
	if pre_condition_158(y=y)==True:
		print("pre_condition_158 SAT")
		print('x = 899/1024')
		print('y = -8423/4096')
		exit(0)
	
	
	if pre_condition_159(y=y)==True:
		print("pre_condition_159 SAT")
		print('x = 119/128')
		print('y = 8329/4096')
		exit(0)
	
	
	if pre_condition_160(y=y)==True:
		print("pre_condition_160 SAT")
		print('x = 1895/2048')
		print('y = 16675/8192')
		exit(0)
	
	
	if pre_condition_161(y=y)==True:
		print("pre_condition_161 SAT")
		print('x = 1997/2048')
		print('y = 4121/2048')
		exit(0)
	
	
	if pre_condition_162(y=y)==True:
		print("pre_condition_162 SAT")
		print('x = 1009/1024')
		print('y = 8221/4096')
		exit(0)
	
	
	if pre_condition_163(y=y)==True:
		print("pre_condition_163 SAT")
		print('x = 18307/8192')
		print('y = 151/2048')
		exit(0)
	
	
	if pre_condition_164(y=y)==True:
		print("pre_condition_164 SAT")
		print('x = 1823/2048')
		print('y = -16803/8192')
		exit(0)
	
	
	if pre_condition_165(y=y)==True:
		print("pre_condition_165 SAT")
		print('x = 253/256')
		print('y = 8215/4096')
		exit(0)
	
	
	if pre_condition_166(y=y)==True:
		print("pre_condition_166 SAT")
		print('x = 18309/8192')
		print('y = 135/2048')
		exit(0)
	
	
	if pre_condition_167(y=y)==True:
		print("pre_condition_167 SAT")
		print('x = 469/512')
		print('y = 8355/4096')
		exit(0)
	
	
	if pre_condition_168(y=y)==True:
		print("pre_condition_168 SAT")
		print('x = 951/1024')
		print('y = 8331/4096')
		exit(0)
	
	
	if pre_condition_169(y=y)==True:
		print("pre_condition_169 SAT")
		print('x = 225/256')
		print('y = -8421/4096')
		exit(0)
	
	
	if pre_condition_170(y=y)==True:
		print("pre_condition_170 SAT")
		print('x = 1989/2048')
		print('y = 8249/4096')
		exit(0)
	
	
	if pre_condition_171(y=y)==True:
		print("pre_condition_171 SAT")
		print('x = 1993/2048')
		print('y = 4123/2048')
		exit(0)
	
	
	if pre_condition_172(y=y)==True:
		print("pre_condition_172 SAT")
		print('x = 451/512')
		print('y = -4209/2048')
		exit(0)
	
	
	if pre_condition_173(y=y)==True:
		print("pre_condition_173 SAT")
		print('x = 2037/2048')
		print('y = 4101/2048')
		exit(0)
	
	
	if pre_condition_174(y=y)==True:
		print("pre_condition_174 SAT")
		print('x = 999/1024')
		print('y = 8241/4096')
		exit(0)
	
	
	if pre_condition_175(y=y)==True:
		print("pre_condition_175 SAT")
		print('x = 63/64')
		print('y = 8223/4096')
		exit(0)
	
	
	if pre_condition_176(y=y)==True:
		print("pre_condition_176 SAT")
		print('x = 1867/2048')
		print('y = -8363/4096')
		exit(0)
	
	
	if pre_condition_177(y=y)==True:
		print("pre_condition_177 SAT")
		print('x = 1893/2048')
		print('y = 8339/4096')
		exit(0)
	
	
	if pre_condition_178(y=y)==True:
		print("pre_condition_178 SAT")
		print('x = 1811/2048')
		print('y = -2103/1024')
		exit(0)
	
	
	if pre_condition_179(y=y)==True:
		print("pre_condition_179 SAT")
		print('x = 249/256')
		print('y = -8247/4096')
		exit(0)
	
	
	if pre_condition_180(y=y)==True:
		print("pre_condition_180 SAT")
		print('x = 1851/2048')
		print('y = -8377/4096')
		exit(0)
	
	
	if pre_condition_181(y=y)==True:
		print("pre_condition_181 SAT")
		print('x = 499/512')
		print('y = 8243/4096')
		exit(0)
	
	
	if pre_condition_182(y=y)==True:
		print("pre_condition_182 SAT")
		print('x = 1019/1024')
		print('y = 8201/4096')
		exit(0)
	
	
	if pre_condition_183(y=y)==True:
		print("pre_condition_183 SAT")
		print('x = 1805/2048')
		print('y = -8417/4096')
		exit(0)
	
	
	if pre_condition_184(y=y)==True:
		print("pre_condition_184 SAT")
		print('x = 509/512')
		print('y = 8203/4096')
		exit(0)
	
	
	if pre_condition_185(y=y)==True:
		print("pre_condition_185 SAT")
		print('x = 4579/2048')
		print('y = 1/32')
		exit(0)
	
	
	if pre_condition_186(y=y)==True:
		print("pre_condition_186 SAT")
		print('x = 1803/2048')
		print('y = -8419/4096')
		exit(0)
	
	
	if pre_condition_187(y=y)==True:
		print("pre_condition_187 SAT")
		print('x = 233/256')
		print('y = -8365/4096')
		exit(0)
	
	
	if pre_condition_188(y=y)==True:
		print("pre_condition_188 SAT")
		print('x = 997/1024')
		print('y = 8245/4096')
		exit(0)
	
	
	if pre_condition_189(y=y)==True:
		print("pre_condition_189 SAT")
		print('x = 1837/2048')
		print('y = -8389/4096')
		exit(0)
	
	
	if pre_condition_190(y=y)==True:
		print("pre_condition_190 SAT")
		print('x = 1991/2048')
		print('y = -16495/8192')
		exit(0)
	
	
	if pre_condition_191(y=y)==True:
		print("pre_condition_191 SAT")
		print('x = 1813/2048')
		print('y = -4205/2048')
		exit(0)
	
	
	if pre_condition_192(y=y)==True:
		print("pre_condition_192 SAT")
		print('x = 18313/8192')
		print('y = 3/64')
		exit(0)
	
	
	if pre_condition_193(y=y)==True:
		print("pre_condition_193 SAT")
		print('x = 113/128')
		print('y = -4207/2048')
		exit(0)
	
	
	if pre_condition_194(y=y)==True:
		print("pre_condition_194 SAT")
		print('x = 127/128')
		print('y = 8207/4096')
		exit(0)
	
	
	if pre_condition_195(y=y)==True:
		print("pre_condition_195 SAT")
		print('x = 2289/1024')
		print('y = 7/128')
		exit(0)
	
	
	if pre_condition_196(y=y)==True:
		print("pre_condition_196 SAT")
		print('x = 505/512')
		print('y = -8219/4096')
		exit(0)
	
	
	if pre_condition_197(y=y)==True:
		print("pre_condition_197 SAT")
		print('x = 507/512')
		print('y = -8211/4096')
		exit(0)
	
	
	if pre_condition_198(y=y)==True:
		print("pre_condition_198 SAT")
		print('x = 1013/1024')
		print('y = -8213/4096')
		exit(0)
	
	
	if pre_condition_199(y=y)==True:
		print("pre_condition_199 SAT")
		print('x = 1871/2048')
		print('y = -8359/4096')
		exit(0)
	
	
	if pre_condition_200(y=y)==True:
		print("pre_condition_200 SAT")
		print('x = 1807/2048')
		print('y = -8415/4096')
		exit(0)
	
	
	if pre_condition_201(y=y)==True:
		print("pre_condition_201 SAT")
		print('x = 1841/2048')
		print('y = 4193/2048')
		exit(0)
	
	
	if pre_condition_202(y=y)==True:
		print("pre_condition_202 SAT")
		print('x = 905/1024')
		print('y = 8413/4096')
		exit(0)
	
	
	if pre_condition_203(y=y)==True:
		print("pre_condition_203 SAT")
		print('x = 18311/8192')
		print('y = 29/512')
		exit(0)
	
	
	if pre_condition_204(y=y)==True:
		print("pre_condition_204 SAT")
		print('x = 1017/1024')
		print('y = 8205/4096')
		exit(0)
	
	
	if pre_condition_205(y=y)==True:
		print("pre_condition_205 SAT")
		print('x = 1015/1024')
		print('y = 8209/4096')
		exit(0)
	
	
	if pre_condition_206(y=y)==True:
		print("pre_condition_206 SAT")
		print('x = 1809/2048')
		print('y = -16827/8192')
		exit(0)
	
	
	if pre_condition_207(y=y)==True:
		print("pre_condition_207 SAT")
		print('x = 453/512')
		print('y = -8411/4096')
		exit(0)
	
	
	if pre_condition_208(y=y)==True:
		print("pre_condition_208 SAT")
		print('x = 487/512')
		print('y = 259/128')
		exit(0)
	
	
	if pre_condition_209(y=y)==True:
		print("pre_condition_209 SAT")
		print('x = 907/1024')
		print('y = -8409/4096')
		exit(0)
	
	
	if pre_condition_210(y=y)==True:
		print("pre_condition_210 SAT")
		print('x = 1965/2048')
		print('y = 517/256')
		exit(0)
	
	
	if pre_condition_211(y=y)==True:
		print("pre_condition_211 SAT")
		print('x = 1931/2048')
		print('y = 519/256')
		exit(0)
	
	
	if pre_condition_212(y=y)==True:
		print("pre_condition_212 SAT")
		print('x = 1957/2048')
		print('y = 1035/512')
		exit(0)
	
	
	if pre_condition_213(y=y)==True:
		print("pre_condition_213 SAT")
		print('x = 1875/2048')
		print('y = 16711/8192')
		exit(0)
	
	
	if pre_condition_214(y=y)==True:
		print("pre_condition_214 SAT")
		print('x = 1815/2048')
		print('y = -16817/8192')
		exit(0)
	
	
	if pre_condition_215(y=y)==True:
		print("pre_condition_215 SAT")
		print('x = 1849/2048')
		print('y = -8379/4096')
		exit(0)
	
	
	if pre_condition_216(y=y)==True:
		print("pre_condition_216 SAT")
		print('x = 1961/2048')
		print('y = 2069/1024')
		exit(0)
	
	
	if pre_condition_217(y=y)==True:
		print("pre_condition_217 SAT")
		print('x = 913/1024')
		print('y = -8399/4096')
		exit(0)
	
	
	if pre_condition_218(y=y)==True:
		print("pre_condition_218 SAT")
		print('x = 1923/2048')
		print('y = -1039/512')
		exit(0)
	
	
	if pre_condition_219(y=y)==True:
		print("pre_condition_219 SAT")
		print('x = 1845/2048')
		print('y = 4191/2048')
		exit(0)
	
	
	if pre_condition_220(y=y)==True:
		print("pre_condition_220 SAT")
		print('x = 921/1024')
		print('y = -8385/4096')
		exit(0)
	
	
	if pre_condition_221(y=y)==True:
		print("pre_condition_221 SAT")
		print('x = 9157/4096')
		print('y = 5/128')
		exit(0)
	
	
	if pre_condition_222(y=y)==True:
		print("pre_condition_222 SAT")
		print('x = 115/128')
		print('y = 8387/4096')
		exit(0)
	
	
	if pre_condition_223(y=y)==True:
		print("pre_condition_223 SAT")
		print('x = 229/256')
		print('y = -4197/2048')
		exit(0)
	
	
	if pre_condition_224(y=y)==True:
		print("pre_condition_224 SAT")
		print('x = 1839/2048')
		print('y = -16775/8192')
		exit(0)
	
	
	if pre_condition_225(y=y)==True:
		print("pre_condition_225 SAT")
		print('x = 915/1024')
		print('y = -8395/4096')
		exit(0)
	
	
	if pre_condition_226(y=y)==True:
		print("pre_condition_226 SAT")
		print('x = 18315/8192')
		print('y = 17/512')
		exit(0)
	
	
	if pre_condition_227(y=y)==True:
		print("pre_condition_227 SAT")
		print('x = 1831/2048')
		print('y = -16789/8192')
		exit(0)
	
	
	if pre_condition_228(y=y)==True:
		print("pre_condition_228 SAT")
		print('x = 1833/2048')
		print('y = 8393/4096')
		exit(0)
	
	
	if pre_condition_229(y=y)==True:
		print("pre_condition_229 SAT")
		print('x = 485/512')
		print('y = 1037/512')
		exit(0)
	
	
	if pre_condition_230(y=y)==True:
		print("pre_condition_230 SAT")
		print('x = 987/1024')
		print('y = 1033/512')
		exit(0)
	
	
	if pre_condition_231(y=y)==True:
		print("pre_condition_231 SAT")
		print('x = 949/1024')
		print('y = 8335/4096')
		exit(0)
	
	
	if pre_condition_232(y=y)==True:
		print("pre_condition_232 SAT")
		print('x = 985/1024')
		print('y = 2067/1024')
		exit(0)
	
	
	if pre_condition_233(y=y)==True:
		print("pre_condition_233 SAT")
		print('x = 1953/2048')
		print('y = -2071/1024')
		exit(0)
	
	
	if pre_condition_234(y=y)==True:
		print("pre_condition_234 SAT")
		print('x = 989/1024')
		print('y = 2065/1024')
		exit(0)
	
	
	if pre_condition_235(y=y)==True:
		print("pre_condition_235 SAT")
		print('x = 923/1024')
		print('y = -8381/4096')
		exit(0)
	
	
	if pre_condition_236(y=y)==True:
		print("pre_condition_236 SAT")
		print('x = 475/512')
		print('y = 8333/4096')
		exit(0)
	
	
	if pre_condition_237(y=y)==True:
		print("pre_condition_237 SAT")
		print('x = 939/1024')
		print('y = -8353/4096')
		exit(0)
	
	
	if pre_condition_238(y=y)==True:
		print("pre_condition_238 SAT")
		print('x = 1847/2048')
		print('y = -16761/8192')
		exit(0)
	
	
	if pre_condition_239(y=y)==True:
		print("pre_condition_239 SAT")
		print('x = 461/512')
		print('y = 8383/4096')
		exit(0)
	
	
	if pre_condition_240(y=y)==True:
		print("pre_condition_240 SAT")
		print('x = 247/256')
		print('y = 4131/2048')
		exit(0)
	
	
	if pre_condition_241(y=y)==True:
		print("pre_condition_241 SAT")
		print('x = 1865/2048')
		print('y = 535303/262144')
		exit(0)
	
	
	if pre_condition_242(y=y)==True:
		print("pre_condition_242 SAT")
		print('x = 121/128')
		print('y = 2075/1024')
		exit(0)
	
	
	if pre_condition_243(y=y)==True:
		print("pre_condition_243 SAT")
		print('x = 243/256')
		print('y = 2073/1024')
		exit(0)
	
	
	if pre_condition_244(y=y)==True:
		print("pre_condition_244 SAT")
		print('x = 1889/2048')
		print('y = 8343/4096')
		exit(0)
	
	
	if pre_condition_245(y=y)==True:
		print("pre_condition_245 SAT")
		print('x = 1869/2048')
		print('y = -8361/4096')
		exit(0)
	
	
	if pre_condition_246(y=y)==True:
		print("pre_condition_246 SAT")
		print('x = 959/1024')
		print('y = 2079/1024')
		exit(0)
	
	
	if pre_condition_247(y=y)==True:
		print("pre_condition_247 SAT")
		print('x = 969/1024')
		print('y = -4149/2048')
		exit(0)
	
	
	if pre_condition_248(y=y)==True:
		print("pre_condition_248 SAT")
		print('x = 1873/2048')
		print('y = -8357/4096')
		exit(0)
	
	
	if pre_condition_249(y=y)==True:
		print("pre_condition_249 SAT")
		print('x = 1913/2048')
		print('y = 8321/4096')
		exit(0)
	
	
	if pre_condition_250(y=y)==True:
		print("pre_condition_250 SAT")
		print('x = 477/512')
		print('y = -4163/2048')
		exit(0)
	
	
	if pre_condition_251(y=y)==True:
		print("pre_condition_251 SAT")
		print('x = 471/512')
		print('y = -8347/4096')
		exit(0)
	
	
	if pre_condition_252(y=y)==True:
		print("pre_condition_252 SAT")
		print('x = 1927/2048')
		print('y = 2077/1024')
		exit(0)
	
	
	if pre_condition_253(y=y)==True:
		print("pre_condition_253 SAT")
		print('x = 493/512')
		print('y = 4133/2048')
		exit(0)
	
	
	if pre_condition_254(y=y)==True:
		print("pre_condition_254 SAT")
		print('x = 1973/2048')
		print('y = 8265/4096')
		exit(0)
	
	
	if pre_condition_255(y=y)==True:
		print("pre_condition_255 SAT")
		print('x = 1885/2048')
		print('y = -16693/8192')
		exit(0)
	
	
	if pre_condition_256(y=y)==True:
		print("pre_condition_256 SAT")
		print('x = 235/256')
		print('y = -8351/4096')
		exit(0)
	
	
	if pre_condition_257(y=y)==True:
		print("pre_condition_257 SAT")
		print('x = 1911/2048')
		print('y = -8323/4096')
		exit(0)


	print("UNKNOWN")
	exit(0)
