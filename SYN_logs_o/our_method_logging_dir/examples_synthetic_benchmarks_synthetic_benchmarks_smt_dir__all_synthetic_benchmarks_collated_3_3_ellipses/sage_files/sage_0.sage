var('a')
var('b')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((33/64 + lambda_var_0 + ((lambda_var_0)**2) + (-1 * b)) > 0), ((33/64 + lambda_var_0 + ((lambda_var_0)**2) + (-1 * a)) < 0), ((1/512 + lambda_var_0 + ((lambda_var_0)**2) + (-4 * a) + (-2 * a * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

