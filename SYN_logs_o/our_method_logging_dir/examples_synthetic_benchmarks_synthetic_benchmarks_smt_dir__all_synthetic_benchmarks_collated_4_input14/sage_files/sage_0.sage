var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = ((-27/4 + lambda_var_0 + ((lambda_var_0)**2) + ((x)**2)) <= 0)
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

