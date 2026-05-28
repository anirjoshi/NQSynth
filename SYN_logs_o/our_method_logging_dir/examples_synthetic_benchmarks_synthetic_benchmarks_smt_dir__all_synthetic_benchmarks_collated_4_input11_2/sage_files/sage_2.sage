var('c')
var('d')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((-1/4 + c + (1/64 * (((-5 + (8 * lambda_var_0)))**2))) > 0), ((1/2 + d + (-1/64 * (((-5 + (8 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

