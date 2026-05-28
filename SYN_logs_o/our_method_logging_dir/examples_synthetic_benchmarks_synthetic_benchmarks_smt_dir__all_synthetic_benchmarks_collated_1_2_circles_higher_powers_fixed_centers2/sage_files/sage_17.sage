var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((17592186044416 * ((lambda_var_0)**3)) + (22369561214976 * ((lambda_var_0)**2)) + (27073616563003 * lambda_var_0)) > -9217480336053/4194304), ((1/4194304 + (-1 * r2) + (1/17592186044416 * (((1777773 + (4194304 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

