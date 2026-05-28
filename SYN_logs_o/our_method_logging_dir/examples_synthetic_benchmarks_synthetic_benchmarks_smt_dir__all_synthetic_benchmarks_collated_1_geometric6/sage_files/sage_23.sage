var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((55239805082673685495785420993/79228162514264337593543950336 + c + ((lambda_var_0)**2)) < 0), ((38514537870576271983647357121/79228162514264337593543950336 + ((lambda_var_0)**2) + (-1 * ((c)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

