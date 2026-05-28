var('delta')
var('skoX')
var('skoS2')
var('skoSP')
var('skoSM')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((delta >= 0), (lambda_var_0 > -3036954521/2147483648), (skoS2 > 0), (skoX > 0), (skoX < 1), ((delta + skoX) >= 70364482829823/70368744177664), (((skoX)**2) > 0), (delta >= (-2 + ((skoS2)**2))), ((delta + (-1 * skoX)) >= -70364482829823/70368744177664), (delta >= (2 + (-1 * ((skoS2)**2)))), (delta >= (1 + skoX + (-1/4611686018427387904 * (((3036954521 + (2147483648 * lambda_var_0)))**2)))), (delta >= (-1 + (-1 * skoX) + (1/4611686018427387904 * (((3036954521 + (2147483648 * lambda_var_0)))**2)))))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

