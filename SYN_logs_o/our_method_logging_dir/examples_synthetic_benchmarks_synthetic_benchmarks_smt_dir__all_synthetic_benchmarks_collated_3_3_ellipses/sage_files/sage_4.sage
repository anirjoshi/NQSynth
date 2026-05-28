var('a')
var('b')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((1/4 + lambda_var_0 + ((lambda_var_0)**2) + (-1 * b)) > 0), ((1/4 + lambda_var_0 + ((lambda_var_0)**2) + (-1 * a)) < 0), ((1 + (2 * lambda_var_0) + (3 * a) + (-1/8 * (((1 + (2 * lambda_var_0)))**3))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

