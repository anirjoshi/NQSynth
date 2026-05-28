var('r1')
var('r2')
var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((((x)**2) + ((y)**2) + (-1 * r2)) < 0), (((-1 * r1) + (4 * ((x)**2)) + (r1 * ((y)**2))) < 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

