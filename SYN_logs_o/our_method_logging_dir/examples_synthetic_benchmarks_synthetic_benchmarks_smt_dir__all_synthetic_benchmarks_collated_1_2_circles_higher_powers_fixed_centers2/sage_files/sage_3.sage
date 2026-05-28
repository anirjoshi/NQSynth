var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((262144 * ((lambda_var_0)**3)) + (336384 * ((lambda_var_0)**2)) + (406027 * lambda_var_0)) > -17187/512), ((1/256 + (-1 * r2) + (1/262144 * (((219 + (512 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

