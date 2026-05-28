var('r')
var('y')
var('x')
qf = qepcad_formula
F = ((((x)**2) + ((y)**2) + (-1 * r)) <= 0)
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

