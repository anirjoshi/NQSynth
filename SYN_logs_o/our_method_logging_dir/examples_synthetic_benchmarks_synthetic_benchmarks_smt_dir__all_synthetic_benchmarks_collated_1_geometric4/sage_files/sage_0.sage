var('c')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((lambda_var_0 + ((lambda_var_0)**2)) > -655/64), ((3/16 + c + ((lambda_var_0)**2) + (7/8 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

