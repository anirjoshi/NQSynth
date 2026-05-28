var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 217/100), ((2 + (2 * skoS * (-6 + (skoS * (-3 + skoS))))) <= (-1/64 * (1 + (8 * lambda_var_0)) * (8 + ((1 + skoS) * (1 + (8 * lambda_var_0))) + (8 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

