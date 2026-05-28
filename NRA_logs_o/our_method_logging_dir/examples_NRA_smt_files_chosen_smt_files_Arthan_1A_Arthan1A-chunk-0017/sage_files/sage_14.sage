var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= -1/4194304), (skoS >= 199637/262144), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)), ((937168146957/549755813888 + (-39854931769/68719476736 * skoS) + (199637/131072 * lambda_var_0) + (-199637/262144 * skoS * (-4 + (skoS * (2 + skoS))))) >= (-2 + (1/8796093022208 * skoS * (((1 + (4194304 * lambda_var_0)) * (20971521 + (4194304 * lambda_var_0))) + (4194304 * skoS * (12582915 + (4194304 * skoS) + (12582912 * lambda_var_0))))) + (1/8796093022208 * (1 + (4194304 * lambda_var_0)) * (4194305 + (4194304 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

