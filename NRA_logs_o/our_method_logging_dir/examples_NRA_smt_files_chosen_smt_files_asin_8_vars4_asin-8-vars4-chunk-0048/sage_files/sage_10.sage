var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -501/512), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -46566017/1073741824), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 46566017/1073741824), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/262144 * (((501 + (512 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/262144 * (((501 + (512 * lambda_var_0)))**2)))), ((1779587/1310720 + (2108673/655360 * skoS2)) > (1/20480 * (65 + (126 * skoS2)) * (501 + (512 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

