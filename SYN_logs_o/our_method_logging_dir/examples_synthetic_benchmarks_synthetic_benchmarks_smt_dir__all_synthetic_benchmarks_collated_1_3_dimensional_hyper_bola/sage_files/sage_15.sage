var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-120 + a + (((10 + lambda_var_0))**2)) < 0), ((-4 + ((a)**2) + (((10 + lambda_var_0))**2) + (-2 * a * (10 + lambda_var_0))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

