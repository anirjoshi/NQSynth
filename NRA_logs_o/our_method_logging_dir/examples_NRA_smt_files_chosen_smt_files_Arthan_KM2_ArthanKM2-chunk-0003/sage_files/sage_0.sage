var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), ((5/16 + (-1/4 * lambda_var_0) + (1/16 * skoS) + (1/4 * skoS * (-3 + (skoS * (3 + skoS))))) > (-2 + (-1/2 * lambda_var_0 * (-6 + lambda_var_0)) + (-1/2 * skoS * (12 + ((-6 + lambda_var_0) * (6 + lambda_var_0)) + (2 * skoS * (-12 + (2 * skoS) + (3 * lambda_var_0))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

