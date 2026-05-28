var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((4294967296 * ((lambda_var_0)**3)) + (5461573632 * ((lambda_var_0)**2)) + (6609985819 * lambda_var_0)) > -2265543067/65536), ((1/65536 + (-1 * r2) + (1/4294967296 * (((27779 + (65536 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

