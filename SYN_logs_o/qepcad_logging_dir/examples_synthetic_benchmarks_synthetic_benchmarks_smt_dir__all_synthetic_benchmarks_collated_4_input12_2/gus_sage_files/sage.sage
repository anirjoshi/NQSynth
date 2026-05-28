var('r')
var('c')
var('x')
var('l')
qf = qepcad_formula
F = qf.and_(((((l)**2) + ((x)**2) + (-1 * ((r)**2))) < 0), ((r + ((l)**2) + ((x)**2) + (-2 * c) + (-2 * c * x)) < 0))
E = qf.exists(['x', 'l'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

