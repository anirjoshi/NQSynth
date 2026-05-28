var('c')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((((x)**2) + ((y)**2) + (-1 * ((c)**2))) < 0), ((3 + c + ((x)**2) + ((y)**2) + (-4 * x)) < 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

