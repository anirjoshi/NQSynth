var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 > 0), (skoSM > 0), (skoSP > 0), (skoX > 0), (skoX < 1), ((1/40 * skoSP * (65 + (126 * skoS2))) > (-1/5 + (1/40 * skoSM * (61 + (126 * skoS2))))), ((1/5 + (-1/40 * skoSM * (61 + (126 * skoS2))) + (1/40 * skoSP * (65 + (126 * skoS2)))) < (1/40 * skoX * (160 + (40 * skoSM) + (40 * skoSP) + (skoX * (8 + (skoSP * (65 + (126 * skoS2))) + (-1 * skoSM * (61 + (126 * skoS2)))))))), ((2/5 + (-1/20 * skoSM * (61 + (126 * skoS2))) + (1/20 * skoSP * (65 + (126 * skoS2)))) < (1/20 * skoX * (160 + (40 * skoSM) + (40 * skoSP) + (-1 * skoX * (-8 + (skoSM * (61 + (126 * skoS2))) + (-1 * skoSP * (65 + (126 * skoS2))) + (20 * skoX * (4 + skoSM + skoSP))))))))
E = qf.exists(['skoSP', 'skoSM'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

