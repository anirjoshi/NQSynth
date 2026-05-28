var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-805306368 * lambda_var_0) + (29791 * a)) < -121782272), ((961/262144 + (-1 * r) + (1/268435456 * (((253 + (16384 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

