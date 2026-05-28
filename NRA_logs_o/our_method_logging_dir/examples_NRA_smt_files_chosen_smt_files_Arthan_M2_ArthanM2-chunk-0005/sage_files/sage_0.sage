var('delta')
var('skoSINS')
var('skoM')
var('skoCOSS')
var('skoS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoM >= 2), (delta >= (-63/64 + ((lambda_var_0)**2) + ((skoSINS)**2) + (1/4 * lambda_var_0))), (delta >= (63/64 + (-1 * ((lambda_var_0)**2)) + (-1 * ((skoSINS)**2)) + (-1/4 * lambda_var_0))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

