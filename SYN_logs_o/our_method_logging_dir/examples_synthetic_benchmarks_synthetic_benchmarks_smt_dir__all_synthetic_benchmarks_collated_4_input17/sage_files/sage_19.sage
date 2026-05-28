var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((4585582635/134217728 + b + ((lambda_var_0)**3) + (154265/512 * ((lambda_var_0)**2)) + (634649211/262144 * lambda_var_0)) > 0), ((22179883/134217728 + a + ((lambda_var_0)**3) + (154265/512 * ((lambda_var_0)**2)) + (634649211/262144 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

