var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -1), (skoS2 > 0), (skoX > 0), (skoX < 1), ((13/8 + (63/20 * skoS2)) > (-1/5 + (1/40 * (1 + lambda_var_0) * (61 + (126 * skoS2))))), ((-3/10 + (61/40 * lambda_var_0) + (63/20 * lambda_var_0 * skoS2)) > (1/40 * skoX * (-240 + (-40 * lambda_var_0) + (-12 * skoX) + (61 * lambda_var_0 * skoX) + (126 * lambda_var_0 * skoS2 * skoX)))), ((-3/5 + (61/20 * lambda_var_0) + (63/10 * lambda_var_0 * skoS2)) > (-1/20 * skoX * (240 + (40 * lambda_var_0) + (skoX * (73 + (126 * skoS2) + (-1 * (1 + lambda_var_0) * (61 + (126 * skoS2))) + (-20 * skoX * (6 + lambda_var_0))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

