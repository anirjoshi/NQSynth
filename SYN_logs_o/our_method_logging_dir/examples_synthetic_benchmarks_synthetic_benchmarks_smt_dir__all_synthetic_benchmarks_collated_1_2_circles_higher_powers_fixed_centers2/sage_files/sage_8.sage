var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((12065825/67108864 + ((lambda_var_0)**2) + (-1 * r2) + (-1/64 * lambda_var_0)) < 0), (((-49153 * lambda_var_0) + (-16384 * ((lambda_var_0)**3)) + (524288 * ((lambda_var_0)**4)) + (3145920 * ((lambda_var_0)**2))) < 31230385/262144))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

