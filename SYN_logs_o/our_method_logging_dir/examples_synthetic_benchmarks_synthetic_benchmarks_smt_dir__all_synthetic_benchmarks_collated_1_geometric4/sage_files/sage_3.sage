var('c')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((2 * c) + (3 * lambda_var_0)) < 9/2), ((((lambda_var_0)**2) + (-6 * lambda_var_0)) < 13/4))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

