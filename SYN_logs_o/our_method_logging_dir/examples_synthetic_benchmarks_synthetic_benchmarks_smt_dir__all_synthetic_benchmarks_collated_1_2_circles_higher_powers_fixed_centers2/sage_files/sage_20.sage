var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((50567562515873/281474976710656 + ((lambda_var_0)**2) + (-1 * r2) + (-1/4096 * lambda_var_0)) < 0), (((-201326593 * lambda_var_0) + (-67108864 * ((lambda_var_0)**3)) + (137438953472 * ((lambda_var_0)**4)) + (824633733120 * ((lambda_var_0)**2))) < 7326760643087/8589934592))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

