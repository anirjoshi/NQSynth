var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((406288971/16777216 + b + ((lambda_var_0)**3) + (-1718679/65536 * ((lambda_var_0)**2)) + (5696683/32768 * lambda_var_0)) > 0), ((-29918645/16777216 + a + ((lambda_var_0)**3) + (-1718679/65536 * ((lambda_var_0)**2)) + (5762219/32768 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

