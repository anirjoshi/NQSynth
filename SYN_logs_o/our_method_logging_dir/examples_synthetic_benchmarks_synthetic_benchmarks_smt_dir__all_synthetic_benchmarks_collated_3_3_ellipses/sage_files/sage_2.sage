var('a')
var('b')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((a > 1/2048), ((-33/64 + a + lambda_var_0 + (-1 * ((lambda_var_0)**2))) > 0), ((-33/64 + b + lambda_var_0 + (-1 * ((lambda_var_0)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

