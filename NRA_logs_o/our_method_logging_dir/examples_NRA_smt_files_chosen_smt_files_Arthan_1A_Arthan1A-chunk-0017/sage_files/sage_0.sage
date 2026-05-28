var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/8), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((-2 + (1/32 * skoS * (((1 + (8 * lambda_var_0)) * (41 + (8 * lambda_var_0))) + (8 * skoS * (27 + (8 * skoS) + (24 * lambda_var_0))))) + (1/32 * (1 + (8 * lambda_var_0)) * (9 + (8 * lambda_var_0)))) <= 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

