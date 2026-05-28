var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-6442450944 * lambda_var_0) + (704969 * a)) < -970178560), ((7921/1048576 + (-1 * r) + (1/17179869184 * (((2107 + (131072 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

