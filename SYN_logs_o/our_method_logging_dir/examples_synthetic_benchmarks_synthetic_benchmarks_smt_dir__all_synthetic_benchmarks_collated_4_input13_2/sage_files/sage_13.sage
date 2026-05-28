var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-31 * lambda_var_0) + (16 * ((lambda_var_0)**2))) < 47/1024), ((-15423/16384 + ((a)**2) + ((b)**2) + (1/1024 * (((-31 + (32 * lambda_var_0)))**2)) + (31/64 * a) + (-1/16 * b * (-31 + (32 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

