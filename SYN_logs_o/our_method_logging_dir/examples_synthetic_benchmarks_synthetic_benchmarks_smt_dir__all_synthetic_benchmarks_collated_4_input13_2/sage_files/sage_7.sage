var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-7 * lambda_var_0) + (4 * ((lambda_var_0)**2))) < 3/8), ((-55/64 + ((a)**2) + ((b)**2) + (1/64 * (((-7 + (8 * lambda_var_0)))**2)) + (3/4 * a) + (-1/4 * b * (-7 + (8 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

