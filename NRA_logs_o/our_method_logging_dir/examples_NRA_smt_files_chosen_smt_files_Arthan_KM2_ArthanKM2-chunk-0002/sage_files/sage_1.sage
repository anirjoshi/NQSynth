var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 9/20), ((139/2 + (1/2 * skoS * (57 + (2 * skoS * (-39 + (2 * skoS)))))) <= (-1/256 * (1 + (8 * lambda_var_0)) * (160 + ((1 + skoS) * (1 + (8 * lambda_var_0))) + (16 * skoS * (-3 + (skoS * (3 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

