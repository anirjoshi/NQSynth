var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((343 * a) + (1572864 * lambda_var_0)) > 167008), ((49/4096 + (-1 * r) + (1/268435456 * (((991 + (16384 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

