var('delta')
var('skoX')
var('pi')
var('skoSP')
var('skoSM')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), ((skoX * (4 + skoSM + skoSP)) < 0))
E = qf.exists(['skoSP', 'skoSM'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

