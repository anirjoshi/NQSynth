var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((197529645785/1099511627776 + ((lambda_var_0)**2) + (-1 * r2) + (-1/2048 * lambda_var_0)) < 0), (((-50331649 * lambda_var_0) + (-16777216 * ((lambda_var_0)**3)) + (17179869184 * ((lambda_var_0)**4)) + (103079221248 * ((lambda_var_0)**2))) < 30235615459/16777216))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

