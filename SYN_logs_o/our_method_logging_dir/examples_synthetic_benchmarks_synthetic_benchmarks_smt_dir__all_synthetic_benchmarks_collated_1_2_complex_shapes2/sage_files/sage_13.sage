var('a')
var('r')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_(((1048073/268435456 + ((lambda_var_0)**2) + (-1 * r) + (31/256 * lambda_var_0)) < 0), ((7433/8192 + (1/134217728 * a * (((31 + (512 * lambda_var_0)))**3))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

