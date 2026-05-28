var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3160481033833/17592186044416 + ((lambda_var_0)**2) + (-1 * r2) + (-1/1024 * lambda_var_0)) < 0), (((-12582913 * lambda_var_0) + (-4194304 * ((lambda_var_0)**3)) + (2147483648 * ((lambda_var_0)**4)) + (12884904960 * ((lambda_var_0)**2))) < 9217480336053/8589934592))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

