var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 > 0), (skoSM > 0), (skoSP > 0), (skoX > 0), (skoX < 1),  qf.or_((delta < (1 + skoX + (-1 * ((skoSP)**2)))), (delta < (-1 + ((skoSP)**2) + (-1 * skoX)))))
E = qf.exists(['skoSP', 'skoSM'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

