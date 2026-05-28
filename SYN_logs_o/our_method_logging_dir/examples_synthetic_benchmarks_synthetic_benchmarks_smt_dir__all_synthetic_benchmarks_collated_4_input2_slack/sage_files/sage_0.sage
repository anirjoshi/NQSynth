var('x')
var('d1')
var('d2')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((d1 + x + (-1 * ((lambda_var_0)**2))) > 0), ((d2 + ((lambda_var_0)**2) + (-1 * x)) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

