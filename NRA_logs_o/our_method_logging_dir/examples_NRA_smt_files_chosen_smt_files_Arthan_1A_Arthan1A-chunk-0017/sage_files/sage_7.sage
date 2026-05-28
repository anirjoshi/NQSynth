var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -1559/2048), ((-1073709055/536870912 + (1/536870912 * skoS * (163841 + (32768 * skoS * (98307 + (32768 * skoS)))))) <= (-1/33554432 * (1559 + (2048 * lambda_var_0)) * (-49153 + (8 * (1 + skoS) * (1559 + (2048 * lambda_var_0))) + (16384 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

