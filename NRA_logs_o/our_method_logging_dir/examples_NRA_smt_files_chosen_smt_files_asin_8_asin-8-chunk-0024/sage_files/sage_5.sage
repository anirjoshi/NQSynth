var('delta')
var('skoX')
var('skoS2')
var('pi')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/4), (skoS2 >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), ((delta + skoX) >= 57/64), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -57/64), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-15/16 + skoX + ((lambda_var_0)**2) + (1/2 * lambda_var_0))), (delta >= (15/16 + (-1 * skoX) + (-1 * ((lambda_var_0)**2)) + (-1/2 * lambda_var_0))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

