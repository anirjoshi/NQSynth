var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3215379842942017737/4611686018427387904 + c + ((lambda_var_0)**2)) < 0), ((2241841160735858889/4611686018427387904 + ((lambda_var_0)**2) + (-1 * ((c)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

