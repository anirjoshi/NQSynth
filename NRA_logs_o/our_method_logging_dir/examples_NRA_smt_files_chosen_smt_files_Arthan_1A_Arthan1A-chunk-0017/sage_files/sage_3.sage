var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -11/16), ((-1047551/524288 + (1/524288 * skoS * (5121 + (1024 * skoS * (3075 + (1024 * skoS)))))) <= (-1/8192 * (11 + (16 * lambda_var_0)) * (-1537 + (32 * (1 + skoS) * (11 + (16 * lambda_var_0))) + (512 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

