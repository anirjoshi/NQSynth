var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -1/2), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= 9/16), (((skoX)**2) > 0), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -9/16), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-3/4 + lambda_var_0 + skoX + ((lambda_var_0)**2))), (delta >= (3/4 + (-1 * lambda_var_0) + (-1 * skoX) + (-1 * ((lambda_var_0)**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

