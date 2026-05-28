var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -46341/32768), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= 65535/65536), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -65535/65536), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/1073741824 * (((46341 + (32768 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/1073741824 * (((46341 + (32768 * lambda_var_0)))**2)))), ((-1987/10240 + (63/5120 * skoS2)) <= (1/1310720 * (65 + (126 * skoS2)) * (46341 + (32768 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

