var('x')
var('y')
qf = qepcad_formula
F = ((-16 + ((x)**2) + ((y)**2)) <= 0)
E = qf.exists(['y'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

