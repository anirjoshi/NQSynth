var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((2 * z) + (17 * lambda_var_0)) < 289/2), ((289/4 + (-1 * (((-17 + lambda_var_0))**2)) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

