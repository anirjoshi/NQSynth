var('a')
var('b')
var('c')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((c > -343), ((a + (-1 * (((-16 + lambda_var_0))**3))) > 0), ((343 + b + (-1 * (((-16 + lambda_var_0))**3))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

