var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((12345719857/68719476736 + ((lambda_var_0)**2) + (-1 * r2) + (-1/512 * lambda_var_0)) < 0), (((-3145729 * lambda_var_0) + (-1048576 * ((lambda_var_0)**3)) + (268435456 * ((lambda_var_0)**4)) + (1610614272 * ((lambda_var_0)**2))) < 2752325463/16777216))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

