var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -97/128), ((-16773119/8388608 + (1/8388608 * skoS * (20481 + (4096 * skoS * (12291 + (4096 * skoS)))))) <= (-1/262144 * (97 + (128 * lambda_var_0)) * (-6145 + (16 * (1 + skoS) * (97 + (128 * lambda_var_0))) + (2048 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

