var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (lambda_var_0 <= skoS), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((2 + (2 * skoS * (6 + (skoS * (6 + skoS))))) > (-1 * lambda_var_0 * (-5 + (lambda_var_0 * (1 + skoS)) + (skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

