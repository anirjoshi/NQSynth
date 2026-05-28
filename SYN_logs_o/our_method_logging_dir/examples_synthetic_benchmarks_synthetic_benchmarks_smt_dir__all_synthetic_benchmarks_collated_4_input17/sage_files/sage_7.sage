var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((275805/32768 + b + ((lambda_var_0)**3) + (1007/32 * ((lambda_var_0)**2)) + (125707/1024 * lambda_var_0)) > 0), ((-51875/32768 + a + ((lambda_var_0)**3) + (1007/32 * ((lambda_var_0)**2)) + (125707/1024 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

