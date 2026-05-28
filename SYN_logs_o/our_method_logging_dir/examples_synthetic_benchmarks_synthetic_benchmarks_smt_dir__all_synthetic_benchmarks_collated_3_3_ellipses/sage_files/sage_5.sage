var('a')
var('b')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((a > -7/24), ((1/4 + ((lambda_var_0)**2) + (-1 * b)) > 0), ((1/4 + ((lambda_var_0)**2) + (-1 * a)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

