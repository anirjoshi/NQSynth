var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((1/64 + (((1 + lambda_var_0))**2) + (-1 * r2)) < 0), ((((lambda_var_0)**3) + (3 * ((lambda_var_0)**2)) + (4 * lambda_var_0)) > -24191/16384))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

