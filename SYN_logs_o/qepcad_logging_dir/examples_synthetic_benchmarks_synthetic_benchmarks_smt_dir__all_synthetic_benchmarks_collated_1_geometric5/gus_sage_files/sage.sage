var('r1')
var('r2')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_((x > 0), ((r2 + y + (x * y)) < 0), ((r1 + ((y)**2) + (-1 * x)) > 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

