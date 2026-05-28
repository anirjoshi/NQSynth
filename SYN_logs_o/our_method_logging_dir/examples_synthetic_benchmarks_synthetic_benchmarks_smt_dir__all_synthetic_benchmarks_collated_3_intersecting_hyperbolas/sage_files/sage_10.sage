var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-1188 + z + ((lambda_var_0)**2) + (3 * lambda_var_0)) < 0), ((-4761 + (((36 + lambda_var_0))**2) + (10 * z)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

