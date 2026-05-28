var('r1')
var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((((r1)**2) + (-1/68719476736 * (((-1 + (262144 * lambda_var_0)))**2))) > 0), ((((r2)**2) + (-1/68719476736 * (((-1 + (262144 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

