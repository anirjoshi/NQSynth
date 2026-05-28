var('delta')
var('skoX')
var('skoS2')
var('pi')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -5419/8192), (skoS2 >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1), ((delta + skoX) >= 150953985/268435456), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -150953985/268435456), (delta >= (2 + (-1 * ((skoS2)**2)))), ((1/16384 * skoX * (96853 + (16384 * lambda_var_0))) >= 0), (delta >= (-1 + skoX + (1/67108864 * (((5419 + (8192 * lambda_var_0)))**2)))), (delta >= (1 + (-1 * skoX) + (-1/67108864 * (((5419 + (8192 * lambda_var_0)))**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

