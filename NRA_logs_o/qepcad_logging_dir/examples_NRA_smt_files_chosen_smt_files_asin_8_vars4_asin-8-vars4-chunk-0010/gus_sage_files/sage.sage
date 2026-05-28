var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 > 0), (skoSM > 0), (skoSP > 0), (skoX > 0), (skoX < 1), (delta >= (-2 + ((skoS2)**2))), (delta >= (2 + (-1 * ((skoS2)**2)))))
E = qf.exists(['skoSM', 'skoSP'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

