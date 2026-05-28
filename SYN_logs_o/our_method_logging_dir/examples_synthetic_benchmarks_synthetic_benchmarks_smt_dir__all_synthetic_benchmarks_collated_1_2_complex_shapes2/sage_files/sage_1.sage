var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-1 + (a * ((lambda_var_0)**3))) < 0), ((1/9 + ((lambda_var_0)**2) + (-1 * r)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

