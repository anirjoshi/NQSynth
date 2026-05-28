var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((828498847209499505/4611686018427387904 + ((lambda_var_0)**2) + (-1 * r2) + (-1/8192 * lambda_var_0)) < 0), (((-805306369 * lambda_var_0) + (-268435456 * ((lambda_var_0)**3)) + (1099511627776 * ((lambda_var_0)**4)) + (6597069791232 * ((lambda_var_0)**2))) < 3956463495385407863/2251799813685248))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

