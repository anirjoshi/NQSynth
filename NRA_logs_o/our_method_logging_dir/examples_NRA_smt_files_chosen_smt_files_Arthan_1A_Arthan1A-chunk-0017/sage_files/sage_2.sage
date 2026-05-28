var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/1024), (skoS >= 11/16), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((13035/8192 + (-121/256 * skoS) + (11/8 * lambda_var_0) + (-11/16 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/524288 * skoS * (((1 + (1024 * lambda_var_0)) * (5121 + (1024 * lambda_var_0))) + (1024 * skoS * (3075 + (1024 * skoS) + (3072 * lambda_var_0))))) + (1/524288 * (1 + (1024 * lambda_var_0)) * (1025 + (1024 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

