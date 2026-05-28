var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoCOSS >= 0), (skoS >= 0), (skoS >= skoSINS), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), (delta >= (-1 + ((skoCOSS)**2) + ((skoSINS)**2))), (delta >= (1 + (-1 * ((skoCOSS)**2)) + (-1 * ((skoSINS)**2)))))
E = qf.exists(['skoCOSS', 'skoSINS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

