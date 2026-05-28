var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-29 + a + (((1 + lambda_var_0))**2)) < 0), ((192 + ((a)**2) + ((lambda_var_0)**2) + (-28 * a)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

