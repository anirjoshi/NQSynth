var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-1381 * lambda_var_0) + (2048 * ((lambda_var_0)**2))) < 1319/8192), ((-7455/65536 + ((a)**2) + ((b)**2) + (1/16777216 * (((-1381 + (4096 * lambda_var_0)))**2)) + (241/128 * b) + (-1/2048 * a * (-1381 + (4096 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

