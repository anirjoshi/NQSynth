var('r')
var('c')
var('x')
var('l')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((17/64 + lambda_var_0 + ((lambda_var_0)**2) + (-1 * ((r)**2))) < 0), ((17/64 + lambda_var_0 + r + ((lambda_var_0)**2) + (-3 * c) + (-2 * c * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

