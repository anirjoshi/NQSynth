var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 9/20), (delta >= (143 + (((-17 + lambda_var_0))**2))), (delta >= (-143 + (-1 * (((-17 + lambda_var_0))**2)))), ((38 + (2 * skoS * (3 + (skoS * (-15 + skoS))))) <= (-1/4 * (-17 + lambda_var_0) * (14 + ((1 + skoS) * (-17 + lambda_var_0)) + (2 * skoS * (-3 + (skoS * (3 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

