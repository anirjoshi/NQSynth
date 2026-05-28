var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -181/128), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= 255/256), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -255/256), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/16384 * (((181 + (128 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/16384 * (((181 + (128 * lambda_var_0)))**2)))), ((-67/640 + (63/320 * skoS2)) <= (1/5120 * (65 + (126 * skoS2)) * (181 + (128 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

