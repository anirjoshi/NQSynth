var('a')
var('b')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((33/64 + ((lambda_var_0)**2) + (-1 * b) + (1/4 * lambda_var_0)) > 0), ((33/64 + ((lambda_var_0)**2) + (-1 * a) + (1/4 * lambda_var_0)) < 0), (((2 * lambda_var_0) + (4 * a) + (-1/512 * (((1 + (8 * lambda_var_0)))**3))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

