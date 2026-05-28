var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-26388279066624 * lambda_var_0) + (5929741 * a)) < -4394825285632), ((32765/268435456 + ((lambda_var_0)**2) + (-1 * r) + (1/4096 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

