var('r1')
var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((1/17592186044416 + ((lambda_var_0)**2) + (-1 * ((r2)**2))) > 0), ((1/17592186044416 + ((lambda_var_0)**2) + (-1 * ((r1)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

