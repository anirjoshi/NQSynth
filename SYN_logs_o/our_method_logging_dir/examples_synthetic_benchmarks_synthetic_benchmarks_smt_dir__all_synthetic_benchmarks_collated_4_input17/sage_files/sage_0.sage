var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((a + lambda_var_0 + ((lambda_var_0)**3)) < 0), ((b + ((lambda_var_0)**3) + (-1 * lambda_var_0)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

