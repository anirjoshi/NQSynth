var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-15/16 + (((3/4 + lambda_var_0))**4)) < 0), ((-3/4 + b + ((a)**2) + ((b)**2) + (1/16 * (((3 + (4 * lambda_var_0)))**2)) + (-1/2 * a * (3 + (4 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

