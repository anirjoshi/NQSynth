var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((z + (1324 * lambda_var_0)) < 1750328), ((1752976 + (-1 * (((-2646 + lambda_var_0))**2)) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

