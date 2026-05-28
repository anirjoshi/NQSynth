var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/536870912), (skoS >= 12776809/16777216), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((7677296091636825/4503599627370496 + (-163246848222481/281474976710656 * skoS) + (12776809/8388608 * lambda_var_0) + (-12776809/16777216 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/144115188075855872 * skoS * (((1 + (536870912 * lambda_var_0)) * (2684354561 + (536870912 * lambda_var_0))) + (536870912 * skoS * (1610612739 + (536870912 * skoS) + (1610612736 * lambda_var_0))))) + (1/144115188075855872 * (1 + (536870912 * lambda_var_0)) * (536870913 + (536870912 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

