var('c')
var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((c + ((y)**2) + (-1 * x * y)) < 0), ((10 + ((y)**2) + (-1 * ((x)**2))) > 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

