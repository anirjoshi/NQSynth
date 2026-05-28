var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 217/100), (delta >= (-63/64 + (((-10 + lambda_var_0))**2))), (delta >= (63/64 + (-1 * (((-10 + lambda_var_0))**2)))), ((-55/32 + (1/32 * skoS * (41 + (8 * skoS * (27 + (8 * skoS)))))) <= (-1/4 * (-10 + lambda_var_0) * (-13 + (4 * skoS * (-4 + (skoS * (2 + skoS)))) + (4 * (1 + skoS) * (-10 + lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

