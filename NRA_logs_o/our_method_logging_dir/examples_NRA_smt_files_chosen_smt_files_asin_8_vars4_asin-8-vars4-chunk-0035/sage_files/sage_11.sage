var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -5/8), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= 185/256), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -185/256), (delta >= (2 + (-1 * ((skoS2)**2)))), ((1/16 * skoX * (95 + (16 * lambda_var_0))) > 0), (delta >= (-1 + skoX + (1/64 * (((5 + (8 * lambda_var_0)))**2)))), (delta >= (1 + (-1 * skoX) + (-1/64 * (((5 + (8 * lambda_var_0)))**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

