var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), ((3/4 + (-1 * lambda_var_0) + (1/4 * skoS) + (1/2 * skoS * (-4 + (skoS * (2 + skoS))))) > (2 + (-2 * skoS * ((skoS * (-3 + skoS + (3 * lambda_var_0))) + ((-2 + lambda_var_0) * (3 + lambda_var_0)))) + (-2 * (-1 + lambda_var_0) * (-2 + lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

