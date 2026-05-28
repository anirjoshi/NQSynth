var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-15 * lambda_var_0) + (8 * ((lambda_var_0)**2))) < 15/8192), ((-57615/65536 + ((a)**2) + ((b)**2) + (1/256 * (((-15 + (16 * lambda_var_0)))**2)) + (89/128 * a) + (-1/8 * b * (-15 + (16 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

