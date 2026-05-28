var('delta')
var('skoSINS')
var('skoM')
var('skoCOSS')
var('skoS')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 >= 0), (skoM >= 2),  qf.or_((delta < (-63/64 + ((skoSINS)**2))), (delta < (63/64 + (-1 * ((skoSINS)**2))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

