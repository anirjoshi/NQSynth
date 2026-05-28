var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((lambda_var_0 + (4 * ((lambda_var_0)**2))) < 63/16), ((-47/64 + c + ((lambda_var_0)**2) + (-23/4 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

