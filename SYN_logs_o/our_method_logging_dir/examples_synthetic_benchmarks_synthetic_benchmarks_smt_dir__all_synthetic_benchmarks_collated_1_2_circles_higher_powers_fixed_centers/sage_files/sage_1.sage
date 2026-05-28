var('r1')
var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((((lambda_var_0)**4) + (-1 * r2)) < 0), ((2 + ((lambda_var_0)**4) + (-1 * r1) + (-4 * lambda_var_0) + (-4 * ((lambda_var_0)**3)) + (6 * ((lambda_var_0)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

