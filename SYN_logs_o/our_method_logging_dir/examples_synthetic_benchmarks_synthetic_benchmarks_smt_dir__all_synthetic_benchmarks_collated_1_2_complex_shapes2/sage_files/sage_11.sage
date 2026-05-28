var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((134217113/17179869184 + ((lambda_var_0)**2) + (-1 * r) + (89/512 * lambda_var_0)) < 0), ((59215/65536 + (1/1073741824 * a * (((89 + (1024 * lambda_var_0)))**3))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

