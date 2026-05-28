var('a')
var('b')
var('c')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((b > 0), ((a + (-1 * ((lambda_var_0)**2))) > 0), ((c + (-1 * ((lambda_var_0)**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

