var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((-11 + ((x)**2) + ((y)**2)) >= 0), ((-25 + ((x)**2) + ((y)**2)) <= 0))
E = qf.exists(['x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

