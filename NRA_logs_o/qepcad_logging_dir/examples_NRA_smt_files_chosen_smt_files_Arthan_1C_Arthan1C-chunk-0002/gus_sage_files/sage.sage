var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 217/100), ((skoSINS * (3 + (2 * skoCOSS) + (-1 * skoS * (-4 + (skoS * (2 + skoS)))) + (-1 * skoSINS * (1 + skoS)))) >= (-2 + (2 * skoCOSS * (1 + skoCOSS)) + (2 * skoS * ((skoCOSS * (5 + skoCOSS)) + (skoS * (3 + skoS + (3 * skoCOSS))))))))
E = qf.exists(['skoCOSS', 'skoSINS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

