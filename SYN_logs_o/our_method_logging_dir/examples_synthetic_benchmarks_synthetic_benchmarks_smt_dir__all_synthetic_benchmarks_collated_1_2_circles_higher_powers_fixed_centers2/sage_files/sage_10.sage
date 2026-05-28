var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((771738377/4294967296 + ((lambda_var_0)**2) + (-1 * r2) + (-1/128 * lambda_var_0)) < 0), (((-196609 * lambda_var_0) + (-65536 * ((lambda_var_0)**3)) + (4194304 * ((lambda_var_0)**4)) + (25166208 * ((lambda_var_0)**2))) < 2265543067/16777216))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

