var('delta')
var('skoSINS')
var('skoM')
var('skoCOSS')
var('skoS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoM >= 2), (((skoM)**2) > 0), (delta >= (-1 + ((skoSINS)**2) + (((-22 + lambda_var_0))**2))), (delta >= (1 + (-1 * ((skoSINS)**2)) + (-1 * (((-22 + lambda_var_0))**2)))), ((2 * skoSINS * ((skoM)**3) * (22 + (-1 * lambda_var_0) + (2 * skoSINS) + (20 * skoM))) <= (8 * ((skoM)**3) * (-484 + (-1 * ((lambda_var_0)**2)) + (-16 * ((skoM)**2)) + (44 * lambda_var_0) + (264 * skoM) + (-12 * lambda_var_0 * skoM)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

