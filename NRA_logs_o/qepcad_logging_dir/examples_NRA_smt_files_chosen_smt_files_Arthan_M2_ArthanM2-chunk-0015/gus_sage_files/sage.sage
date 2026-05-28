var('delta')
var('skoSINS')
var('skoM')
var('skoCOSS')
var('skoS')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoM >= 2), (skoS >= 2), (((skoM)**2) > 0), (delta >= (-1 + ((skoCOSS)**2) + ((skoSINS)**2))), (delta >= (1 + (-1 * ((skoCOSS)**2)) + (-1 * ((skoSINS)**2)))), ((skoSINS * ((skoM)**3) * ((2 * skoCOSS) + (5 * skoM) + (-1 * skoSINS * (1 + skoS)) + (-1 * skoM * skoS * (-3 + (skoS * (3 + skoS)))))) >= (2 * ((skoM)**3) * (((skoCOSS)**2) + (skoM * (skoM + (3 * skoCOSS))) + (skoS * (((skoCOSS)**2) + (3 * skoM * (skoM + (2 * skoCOSS))) + (skoM * skoS * ((3 * skoCOSS) + (3 * skoM) + (skoM * skoS)))))))))
E = qf.exists(['skoCOSS', 'skoS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

