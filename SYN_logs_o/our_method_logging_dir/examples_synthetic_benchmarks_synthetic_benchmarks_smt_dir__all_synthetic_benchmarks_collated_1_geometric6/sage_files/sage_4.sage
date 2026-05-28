var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((2793/4096 + c + ((lambda_var_0)**2) + (-83/32 * lambda_var_0)) < 0), ((((c)**2) + (-1/4096 * (((45 + (64 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

