var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((268435456 * ((lambda_var_0)**3)) + (341557248 * ((lambda_var_0)**2)) + (413301259 * lambda_var_0)) > -281538269/16384), ((1/4096 + (-1 * r2) + (1/268435456 * (((6949 + (16384 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

