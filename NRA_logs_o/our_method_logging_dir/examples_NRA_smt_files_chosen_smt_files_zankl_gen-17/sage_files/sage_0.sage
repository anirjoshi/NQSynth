var('b')
var('delta')
var('a')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (delta >= (-3 + ((b)**3))), (delta >= (-7/4 + lambda_var_0 + ((lambda_var_0)**2))), ((delta + lambda_var_0 + (-1 * b)) >= -1/2), ((b + delta + (-1 * lambda_var_0)) >= 1/2), (delta >= (3 + (-1 * ((b)**3)))), (delta >= (7/4 + (-1 * lambda_var_0) + (-1 * ((lambda_var_0)**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

