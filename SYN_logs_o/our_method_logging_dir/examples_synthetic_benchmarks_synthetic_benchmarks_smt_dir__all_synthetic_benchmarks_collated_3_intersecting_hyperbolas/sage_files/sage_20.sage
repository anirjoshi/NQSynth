var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-14043675 + z + ((lambda_var_0)**2) + (9274 * lambda_var_0)) < 0), ((-142181776 + (((-1325 + lambda_var_0))**2) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

