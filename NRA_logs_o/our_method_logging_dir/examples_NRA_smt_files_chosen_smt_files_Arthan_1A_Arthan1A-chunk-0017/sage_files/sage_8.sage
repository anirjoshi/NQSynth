var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/131072), (skoS >= 3119/4096), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((457572895/268435456 + (-9728161/16777216 * skoS) + (3119/2048 * lambda_var_0) + (-3119/4096 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/8589934592 * skoS * (((1 + (131072 * lambda_var_0)) * (655361 + (131072 * lambda_var_0))) + (131072 * skoS * (393219 + (131072 * skoS) + (393216 * lambda_var_0))))) + (1/8589934592 * (1 + (131072 * lambda_var_0)) * (131073 + (131072 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

