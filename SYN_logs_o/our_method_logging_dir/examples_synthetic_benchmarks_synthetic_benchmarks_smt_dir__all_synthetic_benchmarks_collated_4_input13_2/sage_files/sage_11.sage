var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-27 * lambda_var_0) + (16 * ((lambda_var_0)**2))) < 111/4096), ((-46767/65536 + ((a)**2) + ((b)**2) + (1/1024 * (((-27 + (32 * lambda_var_0)))**2)) + (137/128 * a) + (-1/16 * b * (-27 + (32 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

