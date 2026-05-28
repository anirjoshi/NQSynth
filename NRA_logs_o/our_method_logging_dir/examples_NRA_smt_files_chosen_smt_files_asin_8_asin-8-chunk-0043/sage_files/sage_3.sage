var('delta')
var('skoX')
var('skoS2')
var('pi')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), ((skoX * (1/2 + (-1 * lambda_var_0))) > 0), ((3/20 + (3/2 * pi) + (3 * pi * skoS2)) < (1/5 + (-1/40 * (-3 + (2 * lambda_var_0)) * (-1 + (10 * pi) + (20 * pi * skoS2))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

