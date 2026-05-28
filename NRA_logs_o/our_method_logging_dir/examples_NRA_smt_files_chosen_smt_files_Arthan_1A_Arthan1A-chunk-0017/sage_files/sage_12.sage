var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/524288), (skoS >= 49909/65536), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((29286451473/17179869184 + (-2490908281/4294967296 * skoS) + (49909/32768 * lambda_var_0) + (-49909/65536 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/137438953472 * skoS * (((1 + (524288 * lambda_var_0)) * (2621441 + (524288 * lambda_var_0))) + (524288 * skoS * (1572867 + (524288 * skoS) + (1572864 * lambda_var_0))))) + (1/137438953472 * (1 + (524288 * lambda_var_0)) * (524289 + (524288 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

