var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -3961/4096), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -1090313/16777216), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 1090313/16777216), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/16777216 * (((3961 + (4096 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/16777216 * (((3961 + (4096 * lambda_var_0)))**2)))), ((225079/163840 + (266301/81920 * skoS2)) >= (1/163840 * (65 + (126 * skoS2)) * (3961 + (4096 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

