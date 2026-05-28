var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = ((((r)**2) + (-1/1024 * (((1 + (32 * lambda_var_0)))**2))) > 0)
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

