var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((3371570134439144908066617/4835703278458516698824704 + c + ((lambda_var_0)**2)) < 0), ((2350740836827907687911225/4835703278458516698824704 + ((lambda_var_0)**2) + (-1 * ((c)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

