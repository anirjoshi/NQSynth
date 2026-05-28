var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((65/64 + ((lambda_var_0)**2) + (-1 * r2) + (1/4 * lambda_var_0)) < 0), (((64 * ((lambda_var_0)**3)) + (128 * ((lambda_var_0)**4)) + (193 * lambda_var_0) + (780 * ((lambda_var_0)**2))) < 24191/32))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

