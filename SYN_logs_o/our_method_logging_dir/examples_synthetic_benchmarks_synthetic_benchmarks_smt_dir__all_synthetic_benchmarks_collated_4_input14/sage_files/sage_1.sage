var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = ((-63/4 + ((x)**2) + (((-3 + lambda_var_0))**2)) <= 0)
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

