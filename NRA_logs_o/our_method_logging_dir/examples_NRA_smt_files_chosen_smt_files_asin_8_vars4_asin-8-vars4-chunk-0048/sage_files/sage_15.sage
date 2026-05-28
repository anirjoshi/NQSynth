var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -267649/262144), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= -182182135/4294967296), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= 182182135/4294967296), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (-1 + skoX + (1/68719476736 * (((267649 + (262144 * lambda_var_0)))**2)))), (delta >= (1 + (-1 * skoX) + (-1/68719476736 * (((267649 + (262144 * lambda_var_0)))**2)))), ((833703/524288 + (4040253/1310720 * skoS2)) < (-1/5 + (1/10485760 * (61 + (126 * skoS2)) * (267649 + (262144 * lambda_var_0))))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

