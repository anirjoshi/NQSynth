var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -49909/65536), ((-274877382655/137438953472 + (1/137438953472 * skoS * (2621441 + (524288 * skoS * (1572867 + (524288 * skoS)))))) <= (-1/17179869184 * (49909 + (65536 * lambda_var_0)) * (-786433 + (4 * (1 + skoS) * (49909 + (65536 * lambda_var_0))) + (262144 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

