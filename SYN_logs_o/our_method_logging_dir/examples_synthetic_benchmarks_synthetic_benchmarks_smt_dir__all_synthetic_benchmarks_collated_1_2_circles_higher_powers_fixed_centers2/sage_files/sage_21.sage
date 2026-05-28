var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((281474976710656 * ((lambda_var_0)**3)) + (357912727781376 * ((lambda_var_0)**2)) + (433177651675363 * lambda_var_0)) > -7326760643087/16777216), ((1/67108864 + (-1 * r2) + (1/281474976710656 * (((7111087 + (16777216 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

