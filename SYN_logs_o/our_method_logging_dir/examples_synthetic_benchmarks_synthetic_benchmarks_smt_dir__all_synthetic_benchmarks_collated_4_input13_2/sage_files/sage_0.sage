var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((lambda_var_0)**2) < 63/64), ((-63/64 + ((a)**2) + ((b)**2) + ((lambda_var_0)**2) + (-1/4 * b) + (-2 * a * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

