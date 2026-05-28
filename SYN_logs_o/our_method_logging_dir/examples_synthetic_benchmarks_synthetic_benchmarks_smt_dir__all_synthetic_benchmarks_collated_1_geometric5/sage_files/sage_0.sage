var('r1')
var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((lambda_var_0 > -1), (r2 < 0), ((lambda_var_0 + (-1 * r1)) < -1))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

