var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((lambda_var_0)**2) < 1), ((a + (-3072 * lambda_var_0)) < -512), ((((lambda_var_0)**2) + (-1 * r)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

