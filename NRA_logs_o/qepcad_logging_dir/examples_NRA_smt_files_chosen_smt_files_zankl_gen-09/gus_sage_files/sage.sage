var('b')
var('delta')
var('a')
qf = qepcad_formula
F = qf.and_((delta >= 0), (a < b), (delta >= (-2 + ((b)**2))), ((delta + (2 * a)) >= 1), (delta >= (2 + (-1 * ((b)**2)))), (((-1 * delta) + (2 * a)) <= 1))
E = qf.exists(['a'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

