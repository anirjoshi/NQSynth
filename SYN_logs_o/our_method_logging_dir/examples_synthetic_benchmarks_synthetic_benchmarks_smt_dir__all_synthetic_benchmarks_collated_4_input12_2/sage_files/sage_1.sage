var('r')
var('c')
var('x')
var('l')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((17/64 + r + ((lambda_var_0)**2) + (-3 * c) + (1/4 * lambda_var_0)) < 0), ((17/64 + ((lambda_var_0)**2) + (-1 * ((r)**2)) + (1/4 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

