var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((52680783350343061008153/75557863725914323419136 + c + ((lambda_var_0)**2)) < 0), ((36730325575579796303641/75557863725914323419136 + ((lambda_var_0)**2) + (-1 * ((c)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

