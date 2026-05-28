var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((357070730625/8589934592 + b + ((lambda_var_0)**3) + (931203/2048 * ((lambda_var_0)**2)) + (17146391299/4194304 * lambda_var_0)) > 0), ((-3706522239/8589934592 + a + ((lambda_var_0)**3) + (931203/2048 * ((lambda_var_0)**2)) + (17146391299/4194304 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

