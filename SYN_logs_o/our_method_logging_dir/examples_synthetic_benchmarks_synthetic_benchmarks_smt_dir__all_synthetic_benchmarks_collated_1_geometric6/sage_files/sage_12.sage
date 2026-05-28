var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3140019361480353/4503599627370496 + c + ((lambda_var_0)**2) + (-87427793/33554432 * lambda_var_0)) < 0), ((((c)**2) + (-1/4503599627370496 * (((46789935 + (67108864 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

