var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-8796093022208 * lambda_var_0) + (5527125 * a)) < -4372276707328/3), ((65281/268435456 + ((lambda_var_0)**2) + (-1 * r) + (1/512 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

