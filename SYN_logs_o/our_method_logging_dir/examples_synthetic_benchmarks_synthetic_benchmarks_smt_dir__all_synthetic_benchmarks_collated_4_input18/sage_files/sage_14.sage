var('a')
var('b')
var('c')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((a > -64), ((c + (-1 * (((-4 + lambda_var_0))**3))) > 0), ((64 + b + (-1 * (((-4 + lambda_var_0))**3))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

