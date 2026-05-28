var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((48985/262144 + ((lambda_var_0)**2) + (-1 * r2) + (-1/8 * lambda_var_0)) < 0), (((-769 * lambda_var_0) + (-256 * ((lambda_var_0)**3)) + (1024 * ((lambda_var_0)**4)) + (6168 * ((lambda_var_0)**2))) < 17187/32768))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

