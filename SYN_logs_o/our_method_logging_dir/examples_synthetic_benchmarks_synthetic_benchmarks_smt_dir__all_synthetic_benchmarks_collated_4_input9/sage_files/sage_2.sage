var('r1')
var('r2')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((r2 + (-1 * (((-2 + lambda_var_0))**2))) > 0), ((r1 * (-1 + (((-2 + lambda_var_0))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

