var('a')
var('b')
var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((-1 + ((x)**2) + ((y)**2)) < 0), ((-1 + ((a)**2) + ((b)**2) + ((x)**2) + ((y)**2) + (-2 * a * y) + (-2 * b * x)) < 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

