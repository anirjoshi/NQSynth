var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-3/64 + z + ((lambda_var_0)**2) + (-1/4 * lambda_var_0)) < 0), ((-15/64 + ((lambda_var_0)**2) + (10 * z) + (1/4 * lambda_var_0)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

