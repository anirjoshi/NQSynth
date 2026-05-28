var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-241 * lambda_var_0) + (128 * ((lambda_var_0)**2))) < 1319/131072), ((-14870055/16777216 + ((a)**2) + ((b)**2) + (1/65536 * (((-241 + (256 * lambda_var_0)))**2)) + (1381/2048 * a) + (-1/128 * b * (-241 + (256 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

