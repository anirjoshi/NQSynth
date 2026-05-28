var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3804238865/134217728 + b + ((lambda_var_0)**3) + (-7919519/262144 * ((lambda_var_0)**2)) + (30188113/131072 * lambda_var_0)) > 0), ((-222292975/134217728 + a + ((lambda_var_0)**3) + (-7919519/262144 * ((lambda_var_0)**2)) + (30450257/131072 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

