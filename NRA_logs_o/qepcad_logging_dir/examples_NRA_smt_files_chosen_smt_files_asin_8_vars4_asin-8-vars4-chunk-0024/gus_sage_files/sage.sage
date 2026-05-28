var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 > 0), (skoSM > 0), (skoSP > 0), (skoX > 0), (skoX < 1), ((skoSM + skoSP) > -4), (delta >= (-2 + ((skoS2)**2))), (delta >= (-1 + skoX + ((skoSM)**2))), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1 * ((skoSP)**2)))), (delta >= (-1 + ((skoSP)**2) + (-1 * skoX))), (delta >= (1 + (-1 * skoX) + (-1 * ((skoSM)**2)))))
E = qf.exists(['skoSP', 'skoSM'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

