var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -4056065/4194304), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -285130813121/4398046511104), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 285130813121/4398046511104), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/17592186044416 * (((4056065 + (4194304 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/17592186044416 * (((4056065 + (4194304 * lambda_var_0)))**2)))), ((115230749/83886080 + (27267219/8388608 * skoS2)) >= (1/167772160 * (65 + (126 * skoS2)) * (4056065 + (4194304 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

