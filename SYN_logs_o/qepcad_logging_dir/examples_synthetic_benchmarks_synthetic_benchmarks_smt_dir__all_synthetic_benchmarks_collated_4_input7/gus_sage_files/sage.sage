var('a')
var('b')
var('r')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((-200 + ((r)**2) + (-1 * ((x)**2)) + (-1 * ((y)**2)) + (20 * x) + (20 * y)) > 0), (((((a)**2) * ((x)**2)) + (((b)**2) * ((y)**2)) + (-1 * ((a)**2) * ((b)**2))) < 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

