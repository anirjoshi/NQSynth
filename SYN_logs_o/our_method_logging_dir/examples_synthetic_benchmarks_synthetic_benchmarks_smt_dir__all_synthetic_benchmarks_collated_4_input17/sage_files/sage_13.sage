var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((700185/32768 + b + ((lambda_var_0)**3) + (4187/32 * ((lambda_var_0)**2)) + (847219/1024 * lambda_var_0)) > 0), ((-20711/32768 + a + ((lambda_var_0)**3) + (4187/32 * ((lambda_var_0)**2)) + (847219/1024 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

