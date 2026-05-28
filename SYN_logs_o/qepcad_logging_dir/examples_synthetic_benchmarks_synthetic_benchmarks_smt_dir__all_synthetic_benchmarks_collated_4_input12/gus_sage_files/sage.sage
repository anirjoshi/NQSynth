var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((-8 + ((x)**2) + ((y)**2)) <= 0), ((-2 + ((x)**3) + ((y)**4)) <= 0), ((-2 + ((x)**4) + ((y)**3)) <= 0))
E = qf.exists(['y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

