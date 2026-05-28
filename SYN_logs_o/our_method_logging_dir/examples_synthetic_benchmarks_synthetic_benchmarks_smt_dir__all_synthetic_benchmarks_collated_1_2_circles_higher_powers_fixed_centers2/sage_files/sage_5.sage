var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((67108864 * ((lambda_var_0)**3)) + (85549056 * ((lambda_var_0)**2)) + (103460947 * lambda_var_0)) > -103144841/8192), ((1/1024 + (-1 * r2) + (1/67108864 * (((3481 + (8192 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

