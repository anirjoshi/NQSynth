var('a')
var('b')
var('c')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((c > -8), ((a + (-1 * (((-2 + lambda_var_0))**3))) > 0), ((8 + b + (-1 * (((-2 + lambda_var_0))**3))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

