var('c')
var('d')
var('x')
var('y')
qf = qepcad_formula
F = qf.and_(((d + y + (-1 * ((x)**2))) > 0), ((c + ((x)**2) + (-1 * ((y)**2))) > 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

