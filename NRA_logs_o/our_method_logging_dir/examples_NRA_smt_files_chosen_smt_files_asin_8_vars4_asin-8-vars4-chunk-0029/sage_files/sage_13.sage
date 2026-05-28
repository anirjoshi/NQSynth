var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -67627/65536), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -1113546175/17179869184), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 1113546175/17179869184), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-1 + skoX + (1/4294967296 * (((67627 + (65536 * lambda_var_0)))**2)))), (delta >= (1 + (-1 * skoX) + (-1/4294967296 * (((67627 + (65536 * lambda_var_0)))**2)))), ((1647789/1048576 + (7985439/2621440 * skoS2)) <= (-1/5 + (1/2621440 * (61 + (126 * skoS2)) * (67627 + (65536 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

