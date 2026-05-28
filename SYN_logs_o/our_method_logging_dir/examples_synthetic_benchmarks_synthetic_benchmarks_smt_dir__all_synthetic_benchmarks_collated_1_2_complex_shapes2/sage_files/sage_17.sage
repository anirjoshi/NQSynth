var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((125/128 + (1/8589934592 * a * (((63 + (2048 * lambda_var_0)))**3))) < 0), ((1/65536 + (-1 * r) + (1/4194304 * (((63 + (2048 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

