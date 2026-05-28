var('a')
var('b')
var('c')
var('x')
var('y')
var('z')
qf = qepcad_formula
F = qf.and_(((((x)**3) + ((y)**3) + (-1 * a)) < 0), ((((x)**3) + ((z)**3) + (-1 * b)) < 0), ((((y)**3) + ((z)**3) + (-1 * c)) < 0))
E = qf.exists(['y', 'x', 'z'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

