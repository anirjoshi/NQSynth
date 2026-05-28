var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((53945122151049237200458985/77371252455336267181195264 + c + ((lambda_var_0)**2)) < 0), ((37611853389234257305883881/77371252455336267181195264 + ((lambda_var_0)**2) + (-1 * ((c)**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

