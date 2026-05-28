var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-1750328 + z + ((lambda_var_0)**2) + (-2 * lambda_var_0)) < 0), ((-7001316 + (((-1324 + lambda_var_0))**2) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

