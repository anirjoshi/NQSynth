var('r1')
var('r2')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((4 + ((lambda_var_0)**2) + (-1 * r2)) < 0), (((3 * r1) + (4 * ((lambda_var_0)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

