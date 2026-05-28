var('a')
var('b')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((-1 + ((x)**4) + ((y)**4)) < 0), ((-1 + ((a)**2) + ((b)**2) + ((x)**2) + ((y)**2) + (-2 * a * x) + (-2 * b * y)) < 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

