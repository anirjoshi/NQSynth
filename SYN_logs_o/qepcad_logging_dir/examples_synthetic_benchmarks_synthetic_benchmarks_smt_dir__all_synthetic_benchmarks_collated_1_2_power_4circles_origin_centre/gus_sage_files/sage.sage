var('r1')
var('r2')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((((x)**4) + ((y)**4) + (-1 * r2)) > 0), ((((x)**4) + ((y)**4) + (-1 * r1)) < 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

