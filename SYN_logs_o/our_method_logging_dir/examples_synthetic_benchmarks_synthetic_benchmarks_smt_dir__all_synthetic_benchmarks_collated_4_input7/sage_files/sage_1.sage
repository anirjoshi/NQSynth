var('a')
var('b')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((12017/64 + ((lambda_var_0)**2) + (-1 * ((r)**2)) + (-19 * lambda_var_0)) < 0), (((1/64 * ((a)**2)) + (-1 * ((a)**2) * ((b)**2)) + (1/4 * ((b)**2) * (((1 + (2 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

