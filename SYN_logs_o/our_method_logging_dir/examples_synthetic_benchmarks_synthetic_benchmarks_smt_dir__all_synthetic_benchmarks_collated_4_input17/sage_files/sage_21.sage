var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((321706287531/8589934592 + b + ((lambda_var_0)**3) + (765977/2048 * ((lambda_var_0)**2)) + (13375818619/4194304 * lambda_var_0)) > 0), ((-4711226965/8589934592 + a + ((lambda_var_0)**3) + (765977/2048 * ((lambda_var_0)**2)) + (13375818619/4194304 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

