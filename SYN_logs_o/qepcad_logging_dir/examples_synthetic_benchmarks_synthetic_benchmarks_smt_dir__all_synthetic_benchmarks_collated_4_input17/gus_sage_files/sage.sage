var('a')
var('b')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((a + x + y + ((x)**3) + ((y)**3) + (((x)**2) * ((y)**2))) < 0), ((b + y + ((x)**3) + ((y)**3) + (-1 * x) + (((x)**2) * ((y)**2))) > 0))
E = qf.exists(['x', 'y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

