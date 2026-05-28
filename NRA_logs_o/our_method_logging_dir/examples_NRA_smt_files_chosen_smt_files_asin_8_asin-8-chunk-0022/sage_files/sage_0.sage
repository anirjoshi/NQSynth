var('delta')
var('skoX')
var('pi')
var('skoSP')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (pi > 15707963/5000000), (skoX > 0), (pi < 31415927/10000000), (skoX < 1),  qf.or_((delta < (63/64 + skoX + (-1 * ((lambda_var_0)**2)) + (-1/4 * lambda_var_0))), (delta < (-63/64 + ((lambda_var_0)**2) + (-1 * skoX) + (1/4 * lambda_var_0)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

