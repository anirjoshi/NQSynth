var('delta')
var('skoX')
var('skoS2')
var('pi')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), ((1/20 * skoSP * (1 + (10 * pi) + (20 * pi * skoS2))) < (-1/5 + (1/20 * skoSM * (-1 + (10 * pi) + (20 * pi * skoS2))))))
E = qf.exists(['skoSM', 'skoSP'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

