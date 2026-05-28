var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-239 * lambda_var_0) + (128 * ((lambda_var_0)**2))) < 2735/524288), ((-58494639/67108864 + ((a)**2) + ((b)**2) + (1/65536 * (((-239 + (256 * lambda_var_0)))**2)) + (2935/4096 * a) + (-1/128 * b * (-239 + (256 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

