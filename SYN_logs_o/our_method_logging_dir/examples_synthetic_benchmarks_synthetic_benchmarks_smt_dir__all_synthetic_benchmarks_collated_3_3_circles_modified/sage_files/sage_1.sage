var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-3/4 + a + (1/64 * a * (((1 + (8 * lambda_var_0)))**2))) < 0), (((2 * lambda_var_0) + (4 * a) + (-1/512 * (((1 + (8 * lambda_var_0)))**3))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

