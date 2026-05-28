var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/32768), (skoS >= 1559/2048), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((57185679/33554432 + (-2430481/4194304 * skoS) + (1559/1024 * lambda_var_0) + (-1559/2048 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/536870912 * skoS * (((1 + (32768 * lambda_var_0)) * (163841 + (32768 * lambda_var_0))) + (32768 * skoS * (98307 + (32768 * skoS) + (98304 * lambda_var_0))))) + (1/536870912 * (1 + (32768 * lambda_var_0)) * (32769 + (32768 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

