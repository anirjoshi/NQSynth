var('y')
var('x')
qf = qepcad_formula
F = (x == y)
E = qf.exists(['x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

