var('a')
var('b')
var('x')
var('y')
var('z')
qf = qepcad_formula
F = qf.and_(((((x)**2) + ((y)**2) + ((z)**2) + (-1 * b)) > 0), ((((x)**2) + ((y)**2) + ((z)**2) + (-1 * a)) < 0), (((-1 * ((x)**2)) + (-1 * ((y)**3)) + (2 * y) + (3 * a) + (2 * a * x)) > 0))
E = qf.exists(['x', 'y', 'z'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

