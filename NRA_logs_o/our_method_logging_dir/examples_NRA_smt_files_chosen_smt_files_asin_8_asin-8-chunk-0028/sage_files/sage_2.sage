var('delta')
var('skoX')
var('skoS2')
var('pi')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -3/2), (skoS2 >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), ((delta + skoX) >= 3/4), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -3/4), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-5/4 + skoX + (-1 * ((lambda_var_0)**2)) + (-3 * lambda_var_0))), (delta >= (5/4 + ((lambda_var_0)**2) + (-1 * skoX) + (3 * lambda_var_0))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

