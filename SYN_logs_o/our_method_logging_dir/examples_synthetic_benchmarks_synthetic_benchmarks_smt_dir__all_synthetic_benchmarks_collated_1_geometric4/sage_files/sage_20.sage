var('c')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((4 * ((lambda_var_0)**2)) + (31 * lambda_var_0)) > -1/16), ((-279/64 + c + ((lambda_var_0)**2) + (11/4 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

