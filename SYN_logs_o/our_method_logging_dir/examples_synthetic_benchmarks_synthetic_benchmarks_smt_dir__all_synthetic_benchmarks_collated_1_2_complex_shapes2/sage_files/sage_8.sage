var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((a + (-12582912 * lambda_var_0)) < -1900544), ((5/16384 + ((lambda_var_0)**2) + (-1 * r) + (1/32 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

