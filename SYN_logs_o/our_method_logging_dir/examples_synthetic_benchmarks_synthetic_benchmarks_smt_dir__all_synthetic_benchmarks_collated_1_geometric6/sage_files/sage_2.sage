var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((185/256 + c + ((lambda_var_0)**2) + (-21/8 * lambda_var_0)) < 0), ((((c)**2) + (-1/256 * (((11 + (16 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

