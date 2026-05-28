var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-89 * lambda_var_0) + (128 * ((lambda_var_0)**2))) < 15/512), ((-31/256 + ((a)**2) + ((b)**2) + (1/65536 * (((-89 + (256 * lambda_var_0)))**2)) + (15/8 * b) + (-1/128 * a * (-89 + (256 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

