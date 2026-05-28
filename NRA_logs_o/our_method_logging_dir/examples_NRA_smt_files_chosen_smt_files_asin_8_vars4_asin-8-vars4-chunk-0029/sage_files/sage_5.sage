var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -1057/1024), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -17119/262144), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 17119/262144), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-1 + skoX + (1/1048576 * (((1057 + (1024 * lambda_var_0)))**2)))), (delta >= (1 + (-1 * skoX) + (-1/1048576 * (((1057 + (1024 * lambda_var_0)))**2)))), ((6435/4096 + (6237/2048 * skoS2)) <= (-1/5 + (1/40960 * (61 + (126 * skoS2)) * (1057 + (1024 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

