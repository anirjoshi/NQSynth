var('a')
var('x')
var('y')
var('z')
qf = qepcad_formula
F = qf.and_(((a + ((x)**2) + (-1 * ((z)**2)) + (a * ((y)**2))) < 0), (((-1 * ((x)**2)) + (-1 * ((y)**3)) + (2 * y) + (3 * a) + (2 * a * x)) > 0))
E = qf.exists(['x', 'z', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

