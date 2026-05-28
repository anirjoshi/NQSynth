var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -399275/524288), ((-18014398375264255/9007199254740992 + (1/9007199254740992 * skoS * (671088641 + (134217728 * skoS * (402653187 + (134217728 * skoS)))))) <= (-1/35184372088832 * (399275 + (524288 * lambda_var_0)) * (-201326593 + (128 * (1 + skoS) * (399275 + (524288 * lambda_var_0))) + (67108864 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

