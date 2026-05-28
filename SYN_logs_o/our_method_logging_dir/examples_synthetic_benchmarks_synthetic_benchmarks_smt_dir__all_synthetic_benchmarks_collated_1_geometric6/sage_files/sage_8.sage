var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((11978083865/17179869184 + c + ((lambda_var_0)**2) + (-170757/65536 * lambda_var_0)) < 0), ((((c)**2) + (-1/17179869184 * (((91387 + (131072 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

