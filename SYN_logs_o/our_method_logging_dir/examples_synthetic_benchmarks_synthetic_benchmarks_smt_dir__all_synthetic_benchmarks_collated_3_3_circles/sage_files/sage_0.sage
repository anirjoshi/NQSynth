var('a')
var('b')
var('r2')
var('r3')
var('x')
var('y')
var('r1')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((lambda_var_0 + (4 * ((lambda_var_0)**2))) <= 47/16), ((17/64 + ((a)**2) + ((b)**2) + ((lambda_var_0)**2) + (-1 * a) + (-1 * ((r3)**2)) + (-1/4 * b) + (1/4 * lambda_var_0) + (-2 * b * lambda_var_0)) <= 0), ((17/64 + ((a)**2) + ((b)**2) + ((lambda_var_0)**2) + (-1 * b) + (-1 * ((r2)**2)) + (-1/4 * a) + (1/4 * lambda_var_0) + (-2 * a * lambda_var_0)) <= 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

