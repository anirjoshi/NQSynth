var('delta')
var('skoS')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 217/100), (delta >= (-99 + (-1/64 * (((1 + (8 * lambda_var_0)))**2)))), (delta >= (99 + (1/64 * (((1 + (8 * lambda_var_0)))**2)))), ((265/2 + (20 * lambda_var_0) + (100 * skoS) + (-10 * skoS * (-4 + (skoS * (2 + skoS))))) <= (2 + (-1/32 * skoS * (((1 + (8 * lambda_var_0)) * (41 + (8 * lambda_var_0))) + (8 * skoS * (27 + (8 * skoS) + (24 * lambda_var_0))))) + (-1/32 * (1 + (8 * lambda_var_0)) * (9 + (8 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

