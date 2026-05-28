var('r2')
var('x')
var('y')
var('lambda_var_0')
qf = qepcad_formula
F = qf.and_((((68719476736 * ((lambda_var_0)**3)) + (87381245952 * ((lambda_var_0)**2)) + (105756439699 * lambda_var_0)) > -2752325463/262144), ((1/1048576 + (-1 * r2) + (1/68719476736 * (((111111 + (262144 * lambda_var_0)))**2))) < 0))
E = qf.exists([lambda_var_0],F)
print(qepcad(E, memcells='1000000000 +L5000'))

