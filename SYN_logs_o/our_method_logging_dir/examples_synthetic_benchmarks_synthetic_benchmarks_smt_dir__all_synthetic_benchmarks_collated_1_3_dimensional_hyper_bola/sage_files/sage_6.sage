var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-15 + a + (1/64 * (((25 + (8 * lambda_var_0)))**2))) < 0), ((-4 + ((a)**2) + (1/64 * (((25 + (8 * lambda_var_0)))**2)) + (-1/4 * a * (25 + (8 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

