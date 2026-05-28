var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-137 * lambda_var_0) + (128 * ((lambda_var_0)**2))) < 111/512), ((-295/1024 + ((a)**2) + ((b)**2) + (1/65536 * (((-137 + (256 * lambda_var_0)))**2)) + (27/16 * b) + (-1/128 * a * (-137 + (256 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

