var('c')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-31 * lambda_var_0) + (8 * c)) < 279/8), ((((lambda_var_0)**2) + (10 * lambda_var_0)) < 1/64))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

