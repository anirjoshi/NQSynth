var('z')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-289/4 + z + ((lambda_var_0)**2)) < 0), ((-289 + (10 * z) + (1/4 * (((-17 + (2 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

