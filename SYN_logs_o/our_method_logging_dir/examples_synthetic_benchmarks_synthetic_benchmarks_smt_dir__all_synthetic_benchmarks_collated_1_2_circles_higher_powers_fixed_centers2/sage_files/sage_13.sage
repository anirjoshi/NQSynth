var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((1073741824 * ((lambda_var_0)**3)) + (1365344256 * ((lambda_var_0)**2)) + (1652454787 * lambda_var_0)) > -60936769/32768), ((1/262144 + (-1 * r2) + (1/1073741824 * (((13889 + (32768 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

