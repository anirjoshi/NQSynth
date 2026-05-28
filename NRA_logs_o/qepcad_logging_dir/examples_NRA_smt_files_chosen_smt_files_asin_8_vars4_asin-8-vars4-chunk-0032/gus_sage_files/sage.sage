var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 > 0), (skoSM > 0), (skoSP > 0), (skoX > 0), (skoX < 1), ((1/40 * skoSP * (65 + (126 * skoS2))) > (-1/5 + (1/40 * skoSM * (61 + (126 * skoS2))))))
E = qf.exists(['skoSP', 'skoSM'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

