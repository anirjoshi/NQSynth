var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-3 * lambda_var_0) + (4 * ((lambda_var_0)**2))) < 3/8), ((-15/64 + ((a)**2) + ((b)**2) + (1/64 * (((-3 + (8 * lambda_var_0)))**2)) + (7/4 * b) + (-1/4 * a * (-3 + (8 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

