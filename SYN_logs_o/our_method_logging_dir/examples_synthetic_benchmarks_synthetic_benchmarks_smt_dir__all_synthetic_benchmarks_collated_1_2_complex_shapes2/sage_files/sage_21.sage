var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((509/512 + (1/4398046511104 * a * (((255 + (16384 * lambda_var_0)))**3))) < 0), ((1/1048576 + (-1 * r) + (1/268435456 * (((255 + (16384 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

