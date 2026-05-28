var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-61 * lambda_var_0) + (32 * ((lambda_var_0)**2))) < 71/2048), ((-59607/65536 + ((a)**2) + ((b)**2) + (1/4096 * (((-61 + (64 * lambda_var_0)))**2)) + (77/128 * a) + (-1/32 * b * (-61 + (64 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

