var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 9/20), ((47/256 + (-1/256 * skoS) + (1/16 * lambda_var_0) + (-1/16 * skoS * (-3 + (skoS * (3 + skoS))))) < (2 + (1/2 * skoS * (12 + ((-2 + lambda_var_0) * (10 + lambda_var_0)) + (2 * skoS * ((2 * skoS) + (3 * lambda_var_0))))) + (1/2 * (-2 + lambda_var_0) * (4 + lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

