var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -1), (skoS2 > 0), (skoX > 0), (skoX < 1), ((53/40 + (63/20 * skoS2)) < (1/40 * (1 + lambda_var_0) * (65 + (126 * skoS2)))), ((3/10 + (13/8 * lambda_var_0) + (63/20 * lambda_var_0 * skoS2)) < (1/40 * skoX * (240 + (40 * lambda_var_0) + (-1 * skoX * (53 + (126 * skoS2) + (-1 * (1 + lambda_var_0) * (65 + (126 * skoS2)))))))), ((3/5 + (13/4 * lambda_var_0) + (63/10 * lambda_var_0 * skoS2)) < (1/20 * skoX * (240 + (40 * lambda_var_0) + (-1 * skoX * (53 + (126 * skoS2) + (-1 * (1 + lambda_var_0) * (65 + (126 * skoS2))) + (20 * skoX * (6 + lambda_var_0))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

