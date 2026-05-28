var('c')
var('d')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((c + ((lambda_var_0)**2)) > 0), ((d + (-1 * ((lambda_var_0)**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

