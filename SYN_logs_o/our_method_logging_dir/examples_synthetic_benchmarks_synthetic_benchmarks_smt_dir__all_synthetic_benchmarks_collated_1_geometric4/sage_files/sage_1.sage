var('c')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-1 * lambda_var_0) + (2 * c)) < -3/8), ((lambda_var_0 + (4 * ((lambda_var_0)**2))) < 655/16))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

