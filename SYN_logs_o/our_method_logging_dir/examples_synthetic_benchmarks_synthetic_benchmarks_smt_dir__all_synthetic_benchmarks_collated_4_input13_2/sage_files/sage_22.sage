var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-2935 * lambda_var_0) + (4096 * ((lambda_var_0)**2))) < 2735/16384), ((-8415/65536 + ((a)**2) + ((b)**2) + (1/67108864 * (((-2935 + (8192 * lambda_var_0)))**2)) + (239/128 * b) + (-1/4096 * a * (-2935 + (8192 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

