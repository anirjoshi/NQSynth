var('delta')
var('a')
qf = qepcad_formula
F = qf.and_((delta >= 0), (delta >= (2 + (-4 * ((a)**2)))), (delta >= (-2 + (4 * ((a)**2)))))
E = qf.exists(['a'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

