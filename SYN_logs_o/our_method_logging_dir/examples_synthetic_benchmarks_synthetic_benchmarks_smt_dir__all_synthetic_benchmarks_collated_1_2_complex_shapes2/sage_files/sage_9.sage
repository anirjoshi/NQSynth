var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((5/16384 + ((lambda_var_0)**2) + (-1 * r) + (1/64 * lambda_var_0)) < 0), ((29/32 + (1/2097152 * a * (((1 + (128 * lambda_var_0)))**3))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

