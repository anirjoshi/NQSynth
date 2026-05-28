var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((-2 + (2 * skoS * ((skoS * (6 + skoS + (3 * lambda_var_0))) + ((1 + lambda_var_0) * (6 + lambda_var_0)))) + (2 * (1 + lambda_var_0) * (2 + lambda_var_0))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

