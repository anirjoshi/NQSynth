var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((67108864 * ((lambda_var_0)**3)) + (85352448 * ((lambda_var_0)**2)) + (103294051 * lambda_var_0)) > -31230385/8192), ((1/16384 + (-1 * r2) + (1/67108864 * (((3473 + (8192 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

