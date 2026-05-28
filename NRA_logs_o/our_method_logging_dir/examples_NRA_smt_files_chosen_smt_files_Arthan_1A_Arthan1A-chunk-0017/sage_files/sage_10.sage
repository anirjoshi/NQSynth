var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/262144), (skoS >= 12477/16384), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((3660764277/2147483648 + (-155675529/268435456 * skoS) + (12477/8192 * lambda_var_0) + (-12477/16384 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/34359738368 * skoS * (((1 + (262144 * lambda_var_0)) * (1310721 + (262144 * lambda_var_0))) + (262144 * skoS * (786435 + (262144 * skoS) + (786432 * lambda_var_0))))) + (1/34359738368 * (1 + (262144 * lambda_var_0)) * (262145 + (262144 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

