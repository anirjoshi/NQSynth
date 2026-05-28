var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -64131/65536), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -2916510465/68719476736), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 2916510465/68719476736), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/4294967296 * (((64131 + (65536 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/4294967296 * (((64131 + (65536 * lambda_var_0)))**2)))), ((14229437/10485760 + (16861887/5242880 * skoS2)) > (1/2621440 * (65 + (126 * skoS2)) * (64131 + (65536 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

