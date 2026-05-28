var('delta')
var('skoX')
var('pi')
var('skoSP')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1),  qf.or_((delta < (1 + skoX + (-1 * ((skoSP)**2)))), (delta < (-1 + ((skoSP)**2) + (-1 * skoX)))))
E = qf.exists(['skoSP'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

