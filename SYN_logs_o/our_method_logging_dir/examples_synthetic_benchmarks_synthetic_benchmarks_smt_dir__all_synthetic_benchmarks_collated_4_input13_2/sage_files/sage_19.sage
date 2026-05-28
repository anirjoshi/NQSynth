var('a')
var('b')
var('y')
var('x')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((-237 * lambda_var_0) + (128 * ((lambda_var_0)**2))) < 399/524288), ((-57517455/67108864 + ((a)**2) + ((b)**2) + (1/65536 * (((-237 + (256 * lambda_var_0)))**2)) + (3097/4096 * a) + (-1/128 * b * (-237 + (256 * lambda_var_0)))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

