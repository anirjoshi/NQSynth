var('r1')
var('r2')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((((x)**4) + ((y)**4) + (-1 * r2)) < 0), ((-2 + r1 + (-1 * ((x)**4)) + (-1 * ((y)**4)) + (-6 * ((x)**2)) + (-6 * ((y)**2)) + (4 * x) + (4 * y) + (4 * ((x)**3)) + (4 * ((y)**3))) > 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

