var('r1')
var('r2')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((17/64 + lambda_var_0 + ((lambda_var_0)**2) + (-1 * r2)) < 0), ((1/16 + (-1 * r1) + (1/4 * r1 * (((1 + (2 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

