var('r')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = ((((lambda_var_0)**2) + (-1 * r)) <= 0)
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

