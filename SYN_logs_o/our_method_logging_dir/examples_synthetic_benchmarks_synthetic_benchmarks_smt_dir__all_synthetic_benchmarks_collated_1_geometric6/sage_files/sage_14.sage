var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3215379842942017737/4611686018427387904 + c + ((lambda_var_0)**2) + (-2797689379/1073741824 * lambda_var_0)) < 0), ((((c)**2) + (-1/4611686018427387904 * (((1497277917 + (2147483648 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

