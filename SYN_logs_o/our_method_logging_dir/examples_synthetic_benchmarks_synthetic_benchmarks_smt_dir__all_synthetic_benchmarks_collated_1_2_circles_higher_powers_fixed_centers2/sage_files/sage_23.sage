var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((4611686018427387904 * ((lambda_var_0)**3)) + (5864041970908790784 * ((lambda_var_0)**2)) + (7097182508516278867 * lambda_var_0)) > -3956463495385407863/2147483648), ((1/268435456 + (-1 * r2) + (1/4611686018427387904 * (((910219111 + (2147483648 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

