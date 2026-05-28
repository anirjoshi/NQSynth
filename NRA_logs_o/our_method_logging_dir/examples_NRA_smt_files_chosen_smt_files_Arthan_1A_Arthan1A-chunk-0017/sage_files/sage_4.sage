var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/4096), (skoS >= 97/128), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((445521/262144 + (-9409/16384 * skoS) + (97/64 * lambda_var_0) + (-97/128 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/8388608 * skoS * (((1 + (4096 * lambda_var_0)) * (20481 + (4096 * lambda_var_0))) + (4096 * skoS * (12291 + (4096 * skoS) + (12288 * lambda_var_0))))) + (1/8388608 * (1 + (4096 * lambda_var_0)) * (4097 + (4096 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

