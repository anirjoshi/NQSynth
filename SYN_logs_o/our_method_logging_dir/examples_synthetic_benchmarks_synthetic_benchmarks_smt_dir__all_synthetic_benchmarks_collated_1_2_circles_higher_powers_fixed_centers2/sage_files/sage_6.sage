var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((48354137/268435456 + ((lambda_var_0)**2) + (-1 * r2) + (-1/32 * lambda_var_0)) < 0), (((-12289 * lambda_var_0) + (-4096 * ((lambda_var_0)**3)) + (65536 * ((lambda_var_0)**4)) + (393312 * ((lambda_var_0)**2))) < 281538269/16777216))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

