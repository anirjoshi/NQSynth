var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((-4999/1000 + ((x)**2) + ((y)**2)) > 0), ((-5 + ((x)**2) + ((y)**2)) < 0))
E = qf.exists(['x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

