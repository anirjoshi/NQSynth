var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-100663296 * lambda_var_0) + (1331 * a)) < -15990784), ((125/65536 + ((lambda_var_0)**2) + (-1 * r) + (1/64 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

