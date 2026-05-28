var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 9/20), (delta >= (288 + (((-12 + lambda_var_0))**2))), (delta >= (-288 + (-1 * (((-12 + lambda_var_0))**2)))), ((51/4 + (17/2 * lambda_var_0) + (289/4 * skoS) + (-17/2 * skoS * (-3 + (skoS * (3 + skoS))))) <= (-2 + (-1/2 * skoS * (12 + (lambda_var_0 * (-12 + lambda_var_0)) + (2 * skoS * (-30 + (2 * skoS) + (3 * lambda_var_0))))) + (-1/2 * (-12 + lambda_var_0) * (-6 + lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

