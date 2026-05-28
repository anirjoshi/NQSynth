var('a')
var('x')
var('y')
var('z')
qf = qepcad_formula
F = qf.and_(((a + ((x)**2) + ((y)**2) + (-1 * ((z)**2))) < 0), ((-3 + ((a)**2) + ((x)**2) + ((y)**2) + (-2 * y) + (-2 * a * x)) < 0))
E = qf.exists(['x', 'z', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

