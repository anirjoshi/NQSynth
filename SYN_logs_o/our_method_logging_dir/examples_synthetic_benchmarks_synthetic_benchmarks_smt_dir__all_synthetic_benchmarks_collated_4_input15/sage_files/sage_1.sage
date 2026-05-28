var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((lambda_var_0)**4) < 4095/4096), ((-63/64 + ((a)**2) + ((b)**2) + ((lambda_var_0)**2) + (-1/4 * a) + (-2 * b * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

