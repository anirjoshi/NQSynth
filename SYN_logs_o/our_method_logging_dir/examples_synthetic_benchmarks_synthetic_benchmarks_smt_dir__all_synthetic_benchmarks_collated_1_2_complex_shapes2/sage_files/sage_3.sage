var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((5/256 + ((lambda_var_0)**2) + (-1 * r) + (1/4 * lambda_var_0)) < 0), ((5/8 + (1/512 * a * (((1 + (8 * lambda_var_0)))**3))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

