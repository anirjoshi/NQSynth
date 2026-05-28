var('r1')
var('r2')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((17/64 + ((lambda_var_0)**2) + (-1 * r2) + (1/4 * lambda_var_0)) < 0), (((-1/16 * (((1 + (8 * lambda_var_0)))**2)) + (3/4 * r1)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

