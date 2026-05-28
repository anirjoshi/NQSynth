var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 9/20), (delta >= (-47/64 + lambda_var_0 + ((lambda_var_0)**2))), (delta >= (47/64 + (-1 * lambda_var_0) + (-1 * ((lambda_var_0)**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

