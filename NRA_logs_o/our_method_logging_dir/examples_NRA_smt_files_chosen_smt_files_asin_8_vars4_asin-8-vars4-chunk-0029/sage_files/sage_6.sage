var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -15841/16384), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -270465/4194304), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 270465/4194304), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/268435456 * (((15841 + (16384 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/268435456 * (((15841 + (16384 * lambda_var_0)))**2)))), ((112509/81920 + (133119/40960 * skoS2)) >= (1/655360 * (65 + (126 * skoS2)) * (15841 + (16384 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

