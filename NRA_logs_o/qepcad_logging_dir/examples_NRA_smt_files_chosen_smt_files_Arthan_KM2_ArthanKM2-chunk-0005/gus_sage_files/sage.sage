var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 9/20), (delta >= (-1 + ((skoCOSS)**2) + ((skoSINS)**2))), (delta >= (1 + (-1 * ((skoCOSS)**2)) + (-1 * ((skoSINS)**2)))))
E = qf.exists(['skoSINS', 'skoCOSS'],F)
print(qepcad(E, memcells='1000000000 +L5000'))

