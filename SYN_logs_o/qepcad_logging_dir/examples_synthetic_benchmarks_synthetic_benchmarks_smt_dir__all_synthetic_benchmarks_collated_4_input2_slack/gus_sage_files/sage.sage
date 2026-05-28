var('x')
var('d1')
var('d2')
var('y')
qf = qepcad_formula
F = qf.and_(((d1 + x + (-1 * ((y)**2))) > 0), ((d2 + ((y)**2) + (-1 * x)) > 0))
E = qf.exists(['y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

