var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
qf = qepcad_formula
F = qf.and_((delta >= 0), ((1/4 * skoSINS * (10 + (2 * skoCOSS) + (-1 * skoSINS * (1 + skoS)) + (-2 * skoS * (-3 + (skoS * (3 + skoS)))))) < (2 + (1/2 * skoCOSS * (6 + skoCOSS)) + (1/2 * skoS * (12 + (skoCOSS * (12 + skoCOSS)) + (2 * skoS * (6 + (2 * skoS) + (3 * skoCOSS))))))))
E = qf.exists(['skoCOSS', 'skoSINS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

