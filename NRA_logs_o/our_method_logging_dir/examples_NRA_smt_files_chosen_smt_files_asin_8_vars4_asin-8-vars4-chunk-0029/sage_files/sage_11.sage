var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -33813/32768), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -278323167/4294967296), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 278323167/4294967296), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-1 + skoX + (1/1073741824 * (((33813 + (32768 * lambda_var_0)))**2)))), (delta >= (1 + (-1 * skoX) + (-1/1073741824 * (((33813 + (32768 * lambda_var_0)))**2)))), ((823901/524288 + (3992751/1310720 * skoS2)) <= (-1/5 + (1/1310720 * (61 + (126 * skoS2)) * (33813 + (32768 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

