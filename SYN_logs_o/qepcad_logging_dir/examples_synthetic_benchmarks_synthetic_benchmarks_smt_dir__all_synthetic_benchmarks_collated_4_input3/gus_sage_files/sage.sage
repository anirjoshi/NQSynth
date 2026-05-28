var('c')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((c + ((x)**2) + (-1 * y)) <= 0), ((((x)**2) + ((y)**2) + (-1 * ((c)**2))) <= 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

