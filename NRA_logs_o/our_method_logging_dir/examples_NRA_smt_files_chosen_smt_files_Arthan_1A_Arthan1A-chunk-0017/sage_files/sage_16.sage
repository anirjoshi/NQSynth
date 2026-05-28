var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/134217728), (skoS >= 399275/524288), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((59978848140075/35184372088832 + (-159420525625/274877906944 * skoS) + (399275/262144 * lambda_var_0) + (-399275/524288 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/9007199254740992 * skoS * (((1 + (134217728 * lambda_var_0)) * (671088641 + (134217728 * lambda_var_0))) + (134217728 * skoS * (402653187 + (134217728 * skoS) + (402653184 * lambda_var_0))))) + (1/9007199254740992 * (1 + (134217728 * lambda_var_0)) * (134217729 + (134217728 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

