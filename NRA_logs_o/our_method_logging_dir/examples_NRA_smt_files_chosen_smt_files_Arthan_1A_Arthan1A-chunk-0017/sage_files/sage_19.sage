var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -12776809/16777216), ((-288230375614840831/144115188075855872 + (1/144115188075855872 * skoS * (2684354561 + (536870912 * skoS * (1610612739 + (536870912 * skoS)))))) <= (-1/4503599627370496 * (12776809 + (16777216 * lambda_var_0)) * (-805306369 + (16 * (1 + skoS) * (12776809 + (16777216 * lambda_var_0))) + (268435456 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

