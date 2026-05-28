var('delta')
var('a')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (delta >= (2 + (-1/64 * (((1 + (8 * lambda_var_0)))**2)))), (delta >= (-2 + (1/64 * (((1 + (8 * lambda_var_0)))**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

