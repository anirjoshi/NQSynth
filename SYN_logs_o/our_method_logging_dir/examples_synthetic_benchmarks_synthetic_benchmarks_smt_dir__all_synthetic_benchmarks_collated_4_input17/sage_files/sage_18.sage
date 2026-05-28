var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((4585582635/134217728 + b + ((lambda_var_0)**3) + (-8963543/262144 * ((lambda_var_0)**2)) + (38609735/131072 * lambda_var_0)) > 0), ((22179883/134217728 + a + ((lambda_var_0)**3) + (-8963543/262144 * ((lambda_var_0)**2)) + (38871879/131072 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

