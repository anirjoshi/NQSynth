var('r2')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((((x)**2) + ((y)**2) + (-1 * r2)) < 0), ((2 + ((x)**4) + (-4 * y) + (-4 * ((y)**3)) + (6 * ((x)**2))) < 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

