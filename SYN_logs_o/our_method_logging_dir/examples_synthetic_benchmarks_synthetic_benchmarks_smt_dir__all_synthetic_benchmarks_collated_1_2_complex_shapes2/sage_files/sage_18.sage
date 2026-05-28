var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-17179869184 * lambda_var_0) + (30375 * a)) < -8489271296/3), ((2041/4194304 + ((lambda_var_0)**2) + (-1 * r) + (1/256 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

