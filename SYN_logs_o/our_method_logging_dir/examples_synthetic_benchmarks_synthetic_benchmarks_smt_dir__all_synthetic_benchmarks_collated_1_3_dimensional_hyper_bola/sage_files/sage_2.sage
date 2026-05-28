var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((((a)**2) + (-1 * a)) < 11/4), ((1/4 + a + (-1 * (((-1 + lambda_var_0))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

