var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-8 + ((x)**2) + (((-1 + lambda_var_0))**2)) <= 0), ((-2 + ((x)**3) + (((-1 + lambda_var_0))**4)) <= 0), ((-2 + ((x)**4) + (((-1 + lambda_var_0))**3)) <= 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

