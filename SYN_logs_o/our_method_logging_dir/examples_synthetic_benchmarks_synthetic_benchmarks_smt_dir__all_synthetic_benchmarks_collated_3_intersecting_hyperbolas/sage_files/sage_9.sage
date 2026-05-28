var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-1 * z) + (10 * lambda_var_0)) > -580), ((100 + (-1 * (((68 + lambda_var_0))**2)) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

