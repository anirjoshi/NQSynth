var('r')
var('c')
var('x')
var('l')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((((r)**2) + (-1/1024 * (((1 + (32 * lambda_var_0)))**2))) > 0), ((1/1024 + r + ((lambda_var_0)**2) + (-33/16 * c) + (1/16 * lambda_var_0) + (-2 * c * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

