var('b')
var('delta')
var('a')
qf = qepcad_formula
F = qf.and_((delta >= 0), (delta >= (-2 + ((a)**2))), (delta >= (-3 + ((b)**3))), (delta >= (2 + (-1 * ((a)**2)))), (delta >= (3 + (-1 * ((b)**3)))))
E = qf.exists(['a'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

