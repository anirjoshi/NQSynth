var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3804238865/134217728 + b + ((lambda_var_0)**3) + (121107/512 * ((lambda_var_0)**2)) + (465550627/262144 * lambda_var_0)) > 0), ((-222292975/134217728 + a + ((lambda_var_0)**3) + (121107/512 * ((lambda_var_0)**2)) + (465550627/262144 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

