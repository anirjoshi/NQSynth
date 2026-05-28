var('c')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((53945122151049237200458985/77371252455336267181195264 + c + ((lambda_var_0)**2) + (-11459335696557/4398046511104 * lambda_var_0)) < 0), ((((c)**2) + (-1/77371252455336267181195264 * (((6132850347859 + (8796093022208 * lambda_var_0)))**2))) > 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

