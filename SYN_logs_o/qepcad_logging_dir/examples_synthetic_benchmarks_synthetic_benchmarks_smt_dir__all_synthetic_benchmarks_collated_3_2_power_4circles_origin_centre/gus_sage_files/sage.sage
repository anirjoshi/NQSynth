var('r1')
var('r2')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((((x)**12) + ((y)**12) + (-1 * r2)) > 0), ((((x)**12) + ((y)**12) + (-1 * r1)) < 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

