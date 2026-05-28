var('delta')
var('skoX')
var('pi')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1),  qf.or_((delta < (-1 + skoX + ((skoSM)**2))), (delta < (1 + (-1 * skoX) + (-1 * ((skoSM)**2))))))
E = qf.exists(['skoSM'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

