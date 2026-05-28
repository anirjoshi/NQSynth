var('c')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((-1 + ((x)**2) + ((y)**2)) < 0), ((c + ((x)**2) + ((y)**2) + (-6 * x)) < 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

