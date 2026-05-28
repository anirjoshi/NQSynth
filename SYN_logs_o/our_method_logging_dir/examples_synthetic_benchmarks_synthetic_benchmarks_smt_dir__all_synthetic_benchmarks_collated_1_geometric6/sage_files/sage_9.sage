var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((11978083865/17179869184 + c + ((lambda_var_0)**2)) < 0), ((8351583769/17179869184 + ((lambda_var_0)**2) + (-1 * ((c)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

