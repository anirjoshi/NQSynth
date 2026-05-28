var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((4193345/268435456 + ((lambda_var_0)**2) + (-1 * r) + (-7/32 * lambda_var_0)) < 0), ((5219/8192 + (1/262144 * a * (((-7 + (64 * lambda_var_0)))**3))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

