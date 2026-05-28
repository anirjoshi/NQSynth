var('z')
var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((z + ((y)**2) + (-1 * x * y)) < 0), ((((y)**2) + (-1 * ((x)**2)) + (10 * z)) > 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

