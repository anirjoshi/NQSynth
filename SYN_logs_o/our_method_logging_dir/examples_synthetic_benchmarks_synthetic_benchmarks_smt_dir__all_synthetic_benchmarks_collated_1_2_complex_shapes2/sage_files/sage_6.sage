var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-4194304 * lambda_var_0) + (1125 * a)) < -1605632/3), ((225/16384 + (-1 * r) + (1/16384 * (((5 + (128 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

