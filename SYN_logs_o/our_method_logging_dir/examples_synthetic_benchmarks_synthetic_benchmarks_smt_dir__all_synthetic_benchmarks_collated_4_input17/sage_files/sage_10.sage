var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((286557389/16777216 + b + ((lambda_var_0)**3) + (-1196423/65536 * ((lambda_var_0)**2)) + (2772415/32768 * lambda_var_0)) > 0), ((-15432499/16777216 + a + ((lambda_var_0)**3) + (-1196423/65536 * ((lambda_var_0)**2)) + (2837951/32768 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

