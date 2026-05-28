var('delta')
var('skoX')
var('skoS2')
var('pi')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS2 >= 0), (skoSM >= 0), (skoSP >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), (delta >= (-2 + ((skoS2)**2))), (delta >= (2 + (-1 * ((skoS2)**2)))),  qf.or_((delta < (1 + skoX + (-1 * ((skoSP)**2)))), (delta < (-1 + ((skoSP)**2) + (-1 * skoX)))))
E = qf.exists(['skoSM', 'skoSP'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

