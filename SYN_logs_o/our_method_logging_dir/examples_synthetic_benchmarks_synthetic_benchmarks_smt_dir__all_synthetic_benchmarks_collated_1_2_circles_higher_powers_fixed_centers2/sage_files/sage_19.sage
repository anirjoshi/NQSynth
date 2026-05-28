var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((1099511627776 * ((lambda_var_0)**3)) + (1398096789504 * ((lambda_var_0)**2)) + (1692100368523 * lambda_var_0)) > -30235615459/1048576), ((1/16777216 + (-1 * r2) + (1/1099511627776 * (((444443 + (1048576 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

