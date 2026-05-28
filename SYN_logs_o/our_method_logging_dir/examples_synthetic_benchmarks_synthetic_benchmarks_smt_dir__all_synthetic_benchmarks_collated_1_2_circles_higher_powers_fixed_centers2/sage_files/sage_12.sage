var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((192908417/1073741824 + ((lambda_var_0)**2) + (-1 * r2) + (-1/256 * lambda_var_0)) < 0), (((-786433 * lambda_var_0) + (-262144 * ((lambda_var_0)**3)) + (33554432 * ((lambda_var_0)**4)) + (201327360 * ((lambda_var_0)**2))) < 60936769/262144))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

