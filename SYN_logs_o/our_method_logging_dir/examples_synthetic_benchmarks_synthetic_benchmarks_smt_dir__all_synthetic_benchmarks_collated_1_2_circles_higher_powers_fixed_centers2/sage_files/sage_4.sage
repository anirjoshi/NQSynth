var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((12182897/67108864 + ((lambda_var_0)**2) + (-1 * r2) + (-1/16 * lambda_var_0)) < 0), (((-3073 * lambda_var_0) + (-1024 * ((lambda_var_0)**3)) + (8192 * ((lambda_var_0)**4)) + (49200 * ((lambda_var_0)**2))) < 103144841/16777216))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

