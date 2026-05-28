var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-21 * lambda_var_0) + (16 * ((lambda_var_0)**2))) < 7/64), ((-7/16 + ((a)**2) + ((b)**2) + (-3/2 * a) + (1/1024 * (((-21 + (32 * lambda_var_0)))**2)) + (-1/16 * b * (-21 + (32 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

