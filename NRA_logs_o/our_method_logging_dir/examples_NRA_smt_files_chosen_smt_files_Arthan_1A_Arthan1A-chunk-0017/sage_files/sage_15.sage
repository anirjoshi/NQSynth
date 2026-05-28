var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (skoS >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((lambda_var_0 + (-1 * skoS)) <= -199637/262144), ((-17592181850111/8796093022208 + (1/8796093022208 * skoS * (20971521 + (4194304 * skoS * (12582915 + (4194304 * skoS)))))) <= (-1/549755813888 * (199637 + (262144 * lambda_var_0)) * (-6291457 + (8 * (1 + skoS) * (199637 + (262144 * lambda_var_0))) + (2097152 * skoS * (-4 + (skoS * (2 + skoS))))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

