var('a')
var('r')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((((x)**2) + ((y)**2) + (-1 * r)) < 0), ((1 + (-6 * x) + (a * ((y)**3))) < 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

