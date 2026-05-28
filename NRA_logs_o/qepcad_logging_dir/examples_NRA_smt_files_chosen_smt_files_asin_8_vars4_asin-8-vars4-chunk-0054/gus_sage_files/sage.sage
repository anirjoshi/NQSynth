var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 > 0), (skoSM > 0), (skoSP > 0), (skoX > 0), (skoX < 1), (delta >= (-2 + ((skoS2)**2))), (delta >= (-1 + skoX + ((skoSM)**2))), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1 * ((skoSP)**2)))), (delta >= (-1 + ((skoSP)**2) + (-1 * skoX))), (delta >= (1 + (-1 * skoX) + (-1 * ((skoSM)**2)))), ((1/40 * skoSP * (65 + (126 * skoS2))) >= (-1/5 + (1/40 * skoSM * (61 + (126 * skoS2))))), ((1/5 + (-1/40 * skoSM * (61 + (126 * skoS2))) + (1/40 * skoSP * (65 + (126 * skoS2)))) < (1/40 * skoX * (160 + (40 * skoSM) + (40 * skoSP) + (skoX * (8 + (skoSP * (65 + (126 * skoS2))) + (-1 * skoSM * (61 + (126 * skoS2)))))))))
E = qf.exists(['skoSM', 'skoSP'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

