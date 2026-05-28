var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-31 * lambda_var_0) + (64 * ((lambda_var_0)**2))) < 47/256), ((-63/1024 + ((a)**2) + ((b)**2) + (1/16384 * (((-31 + (128 * lambda_var_0)))**2)) + (31/16 * b) + (-1/64 * a * (-31 + (128 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

