var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-3097 * lambda_var_0) + (4096 * ((lambda_var_0)**2))) < 399/16384), ((-9367/65536 + ((a)**2) + ((b)**2) + (1/67108864 * (((-3097 + (8192 * lambda_var_0)))**2)) + (237/128 * b) + (-1/4096 * a * (-3097 + (8192 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

