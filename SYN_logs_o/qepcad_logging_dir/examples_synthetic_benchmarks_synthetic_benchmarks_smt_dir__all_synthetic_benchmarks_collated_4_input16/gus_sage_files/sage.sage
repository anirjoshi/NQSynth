var('a')
var('b')
var('y')
var('x')
qf = qepcad_formula
F = qf.and_(((((x)**100) + ((y)**100) + (-1 * ((b)**100))) > 0), ((((x)**100) + ((y)**100) + (-1 * ((a)**100))) < 0))
E = qf.exists(['y', 'x'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

