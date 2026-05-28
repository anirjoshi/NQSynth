var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -495/512), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -68673/1048576), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 68673/1048576), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/262144 * (((495 + (512 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/262144 * (((495 + (512 * lambda_var_0)))**2)))), ((11257/8192 + (66591/20480 * skoS2)) >= (1/20480 * (65 + (126 * skoS2)) * (495 + (512 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

