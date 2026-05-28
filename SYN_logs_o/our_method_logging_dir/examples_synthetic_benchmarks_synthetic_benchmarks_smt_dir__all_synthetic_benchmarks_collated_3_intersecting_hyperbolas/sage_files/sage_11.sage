var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-1 * z) + (36 * lambda_var_0)) > -1188), ((1296 + (-1 * (((69 + lambda_var_0))**2)) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

