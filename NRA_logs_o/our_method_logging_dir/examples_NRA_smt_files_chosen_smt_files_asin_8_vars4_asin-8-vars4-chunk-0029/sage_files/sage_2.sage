var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -15/16), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -65/1024), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 65/1024), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/256 * (((15 + (16 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/256 * (((15 + (16 * lambda_var_0)))**2)))), ((1757/1280 + (2079/640 * skoS2)) >= (1/640 * (15 + (16 * lambda_var_0)) * (65 + (126 * skoS2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

