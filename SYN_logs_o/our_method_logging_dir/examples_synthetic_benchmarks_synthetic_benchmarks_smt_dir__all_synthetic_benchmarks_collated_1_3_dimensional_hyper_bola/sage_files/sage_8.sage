var('a')
var('x')
var('y')
var('z')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-25 * a) + (4 * ((a)**2))) < -369/16), ((689/64 + a + (-1 * (((-4 + lambda_var_0))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

