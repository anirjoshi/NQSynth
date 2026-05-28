var('delta')
var('skoS')
var('pi')
var('skoCOSS')
var('skoSINS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (pi < 31415927/10000000), (pi > (2 * skoS)),  qf.or_((delta < (-47/64 + lambda_var_0 + ((lambda_var_0)**2))), (delta < (47/64 + (-1 * lambda_var_0) + (-1 * ((lambda_var_0)**2))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

