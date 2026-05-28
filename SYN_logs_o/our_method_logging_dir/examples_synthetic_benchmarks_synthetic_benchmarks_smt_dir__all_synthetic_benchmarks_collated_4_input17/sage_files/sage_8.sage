var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((448683/32768 + b + ((lambda_var_0)**3) + (-14615/1024 * ((lambda_var_0)**2)) + (26529/512 * lambda_var_0)) > 0), ((-10069/32768 + a + ((lambda_var_0)**3) + (-14615/1024 * ((lambda_var_0)**2)) + (27553/512 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

