var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((skoSINS * (3 + (2 * skoCOSS) + (-1 * skoS * (-4 + (skoS * (2 + skoS)))) + (-1 * skoSINS * (1 + skoS)))) < (-2 + (2 * skoCOSS * (1 + skoCOSS)) + (2 * skoS * ((skoCOSS * (5 + skoCOSS)) + (skoS * (3 + skoS + (3 * skoCOSS))))))))
E = qf.exists(['skoSINS', 'skoCOSS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

