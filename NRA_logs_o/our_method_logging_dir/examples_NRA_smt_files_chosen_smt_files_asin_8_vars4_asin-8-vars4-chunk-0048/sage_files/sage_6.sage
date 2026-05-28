var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -31/32), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -777/16384), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 777/16384), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/1024 * (((31 + (32 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/1024 * (((31 + (32 * lambda_var_0)))**2)))), ((6967/5120 + (8253/2560 * skoS2)) > (1/1280 * (31 + (32 * lambda_var_0)) * (65 + (126 * skoS2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

