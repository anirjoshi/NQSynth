var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), ((2 + (2 * skoS * (-6 + (skoS * (-6 + skoS))))) > (-1/16 * (1 + (2 * lambda_var_0)) * (4 + ((1 + skoS) * (1 + (2 * lambda_var_0))) + (4 * skoS * (-3 + (skoS * (3 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

