var('r')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((-25 + ((x)**2) + ((y)**2)) > 0), ((((x)**2) + ((y)**2) + (-1 * ((r)**2))) < 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

