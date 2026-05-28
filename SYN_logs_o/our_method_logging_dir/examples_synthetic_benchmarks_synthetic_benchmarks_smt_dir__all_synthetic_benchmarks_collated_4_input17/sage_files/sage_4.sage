var('a')
var('b')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((2909/512 + b + ((lambda_var_0)**3) + (-407/64 * ((lambda_var_0)**2)) + (325/32 * lambda_var_0)) > 0), ((-163/512 + a + ((lambda_var_0)**3) + (-407/64 * ((lambda_var_0)**2)) + (389/32 * lambda_var_0)) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

