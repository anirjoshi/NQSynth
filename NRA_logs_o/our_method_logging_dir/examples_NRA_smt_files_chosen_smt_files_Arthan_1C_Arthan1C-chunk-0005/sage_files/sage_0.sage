var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 217/100), (delta >= (3/4 + (-1/64 * (((1 + (8 * lambda_var_0)))**2)))), (delta >= (-3/4 + (1/64 * (((1 + (8 * lambda_var_0)))**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

