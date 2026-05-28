var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -12477/16384), ((-68719214591/34359738368 + (1/34359738368 * skoS * (1310721 + (262144 * skoS * (786435 + (262144 * skoS)))))) <= (-1/2147483648 * (12477 + (16384 * lambda_var_0)) * (-393217 + (8 * (1 + skoS) * (12477 + (16384 * lambda_var_0))) + (131072 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

