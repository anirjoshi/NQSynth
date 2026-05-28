var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((766605563705/1099511627776 + c + ((lambda_var_0)**2) + (-1366059/524288 * lambda_var_0)) < 0), ((((c)**2) + (-1/1099511627776 * (((731093 + (1048576 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

