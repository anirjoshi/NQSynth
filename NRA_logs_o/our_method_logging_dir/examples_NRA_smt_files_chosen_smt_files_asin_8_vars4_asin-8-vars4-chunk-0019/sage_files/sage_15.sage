var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -1/128), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= 67103361/67108864), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -67103361/67108864), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-16383/16384 + skoX + ((lambda_var_0)**2) + (1/64 * lambda_var_0))), (delta >= (16383/16384 + (-1 * skoX) + (-1 * ((lambda_var_0)**2)) + (-1/64 * lambda_var_0))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

