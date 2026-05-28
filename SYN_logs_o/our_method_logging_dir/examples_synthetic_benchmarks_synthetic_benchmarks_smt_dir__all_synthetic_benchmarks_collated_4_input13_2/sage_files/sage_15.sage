var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-119 * lambda_var_0) + (64 * ((lambda_var_0)**2))) < 3119/1048576), ((-58006575/67108864 + ((a)**2) + ((b)**2) + (1/16384 * (((-119 + (128 * lambda_var_0)))**2)) + (3017/4096 * a) + (-1/64 * b * (-119 + (128 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

