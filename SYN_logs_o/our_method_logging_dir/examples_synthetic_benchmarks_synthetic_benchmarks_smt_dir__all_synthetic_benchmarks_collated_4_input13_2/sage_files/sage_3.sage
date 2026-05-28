var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-3 * lambda_var_0) + (2 * ((lambda_var_0)**2))) < 3/8), ((-3/4 + ((a)**2) + ((b)**2) + (-1 * a) + (1/16 * (((-3 + (4 * lambda_var_0)))**2)) + (-1/2 * b * (-3 + (4 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

