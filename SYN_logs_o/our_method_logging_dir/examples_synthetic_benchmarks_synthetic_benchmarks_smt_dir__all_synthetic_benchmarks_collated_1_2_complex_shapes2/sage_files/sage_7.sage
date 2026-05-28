var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((49/64 + (1/2097152 * a * (((15 + (128 * lambda_var_0)))**3))) < 0), ((25/16384 + (-1 * r) + (1/16384 * (((15 + (128 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

