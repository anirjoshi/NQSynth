var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((1183/512 + b + ((lambda_var_0)**3) + (-143/64 * ((lambda_var_0)**2)) + (15/32 * lambda_var_0)) > 0), ((159/512 + a + ((lambda_var_0)**3) + (-143/64 * ((lambda_var_0)**2)) + (79/32 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

