var('delta')
var('skoSINS')
var('skoM')
var('skoCOSS')
var('skoS')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoM >= 2), (skoS >= 2),  qf.or_((delta < (-1 + ((skoCOSS)**2) + ((skoSINS)**2))), (delta < (1 + (-1 * ((skoCOSS)**2)) + (-1 * ((skoSINS)**2))))))
E = qf.exists(['skoS', 'skoCOSS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

