var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((61/64 + (1/16777216 * a * (((11 + (256 * lambda_var_0)))**3))) < 0), ((1/16384 + (-1 * r) + (1/65536 * (((11 + (256 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

