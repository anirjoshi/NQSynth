var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((207124706305601633/1152921504606846976 + ((lambda_var_0)**2) + (-1 * r2) + (-1/16384 * lambda_var_0)) < 0), (((-3221225473 * lambda_var_0) + (-1073741824 * ((lambda_var_0)**3)) + (8796093022208 * ((lambda_var_0)**4)) + (52776558182400 * ((lambda_var_0)**2))) < 1246965652391149073/35184372088832))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

