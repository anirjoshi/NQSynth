var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -2), (skoS2 > 0), (skoX > 0), (skoX < 1), ((53/40 + (63/20 * skoS2)) < (1/40 * (2 + lambda_var_0) * (65 + (126 * skoS2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

