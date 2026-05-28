var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((2 * ((lambda_var_0)**2)) + (3 * lambda_var_0)) < 7/512), ((-583/1024 + ((a)**2) + ((b)**2) + (1/16 * (((3 + (4 * lambda_var_0)))**2)) + (21/16 * b) + (-1/2 * a * (3 + (4 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

