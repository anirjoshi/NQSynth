var('a')
var('r')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((1/4096 + (-1 * r) + (1/16 * (((1 + (2 * lambda_var_0)))**4))) < 0), ((-11023/4096 + (-1 * r) + (2 * ((a)**4)) + (-5/2 * ((a)**3)) + (1/8 * (((1 + (2 * lambda_var_0)))**4)) + (51/128 * (((1 + (2 * lambda_var_0)))**2)) + (63/128 * lambda_var_0) + (115/128 * a) + (3/2 * ((a)**2) * (((1 + (2 * lambda_var_0)))**2)) + (45/16 * a * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

