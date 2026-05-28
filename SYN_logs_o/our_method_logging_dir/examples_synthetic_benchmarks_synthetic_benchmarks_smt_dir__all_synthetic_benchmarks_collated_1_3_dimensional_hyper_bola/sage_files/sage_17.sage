var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((((a)**2) + (-20 * a)) < -96), ((101 + a + (-1 * (((-11 + lambda_var_0))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

