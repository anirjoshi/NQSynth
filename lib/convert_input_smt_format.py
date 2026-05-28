import os
import sys
import copy
import math
import z3
import logging

LE = 1
LT = 0

# rational numbers are represented as numerator and denominator
class rational():
    """
        A class to represent a rational number p/q.
        we represent +- episolon as 0/+-1, and
        0 as 0/1
        +-inf as +-1/0
        nan as 0/0
        Attributes
        ----------
        num : int
            numerator p of the rational no.
        denm : int
            denominator q of the rational no.

        Methods
        -------
        is_not_defined():
            Returns true if p=q=0, otherwise false
        
        is_inf():
            Returns true of p!=0 and q=0, otherwise false

        reduce_lowest():
            Reduces the rational p/q in lowest form

        is_perfect_square():
            Returns True if p/q is of the form r^2/s^2.

        <, +, -, *, /:
            Operations defined       
    """

    #Is the constructor the rational number is (self.num/self.denm)
    def __init__(self, num:int = 0, denm:int = 0):
        self.num = num
        self.denm = denm
        if type(num)==type([]):
            self.num = num[0]
            self.denm = num[1]
        
    def is_not_defined(self):
        #1/0 is +infinity and -1/0 is -infinity
        if self.num == 0 and self.denm == 0:
            return True
        return False
    
    #1/0 is +infinity and -1/0 is -infinity
    def is_inf(self):
        ##equivalent to self.num!=0 and self.denm==0
        if self.is_not_defined() == True:
            return False
        if self.denm == 0:
            if self.num > 0:
                self.num = 1
            elif self.num < 0:
                self.num = -1
            return True
        return False

    def return_string(self):
        return str(self.num)+"/"+str(self.denm)    

    def __repr__(self):
        s = str(self.num)+"/"+str(self.denm)
        return s
       
    #reduce the rational number to the lowest form by dividing self.num
    #and self.denm by its lowest form, assuming the self.num!=0 and self.denm!=0
    def reduce_lowest(self):        
        # print("ANI:81", type(self.num), type(self.denm))

        #represent +- episilon or 0
        if self.num==0 and self.denm!=0:
            self.denm = 1
        
        #represents +-infinity whenever required
        elif self.denm==0: 
            if self.num>0:
                self.num = 1
            if self.num<0:
                self.num = -1
        else:
            d = math.gcd(abs(self.num),abs(self.denm))
            self.num = self.num // d
            self.denm = self.denm // d

            if self.denm<0: #make denominator positive
                self.denm = -1*self.denm
                self.num = -1*self.num
        
            
        return

    def __eq__(self, n1):
        if n1.num==self.num and n1.denm==self.denm: ##optimization
            return True
        else: 
            self.reduce_lowest()
            n1.reduce_lowest()
            return (self.denm==n1.denm) and (self.num==n1.num)  
        
    def __str__(self):
        s = str(self.num)+"/"+str(self.denm)
        return s

    def __lt__ (self, n2):
        
        #self < n2?
        assert(not(\
                    (self.denm==0 and self.num==0)\
                    or (n2.denm==0 and n2.num==0)\
                )\
            )

        #Rational is undefined!
        assert (not(self.denm==0)), "fraction undefined"
        assert (not(n2.denm==0)), "fraction undefined"
        
        
        self.reduce_lowest()
        n2.reduce_lowest()
        
        
        return (self.num*n2.denm) < (n2.num*self.denm)
    
    def __ge__ (self, n2):
        return not(self < n2)

    def __le__ (self, n2):
        return not(n2 < self)
    
    def __gt__ (self, n2):
        return (n2 < self)
         
    def __mul__ (self,n1):
        new_obj = rational()
        new_obj.num = self.num*n1.num
        new_obj.denm = self.denm*n1.denm
        new_obj.reduce_lowest()
        return new_obj
    
    def __sub__(self, n1):
        obj_ret = rational()
        obj_ret.num = (self.num*n1.denm) - (n1.num*self.denm)
        obj_ret.denm = self.denm*n1.denm
        obj_ret.reduce_lowest()
        return obj_ret
    
    def __add__(self, n1):
        obj_ret = rational()
        obj_ret.num = (self.num*n1.denm) + (n1.num*self.denm)
        obj_ret.denm = self.denm*n1.denm
        obj_ret.reduce_lowest()
        return obj_ret
    
    def __Truediv__(self, n1):
        obj_ret = rational()
        obj_ret.num = (self.num*n1.denm)
        obj_ret.denm = self.denm*n1.num
        obj_ret.reduce_lowest()
        return obj_ret
    
    def __div__(self, n1):
        obj_ret = rational()
        obj_ret.num = (self.num*n1.denm)
        obj_ret.denm = self.denm*n1.num
        obj_ret.reduce_lowest()
        return obj_ret

    def __truediv__(self, n1):
        obj_ret = rational()
        obj_ret.num = (self.num*n1.denm)
        obj_ret.denm = self.denm*n1.num
        obj_ret.reduce_lowest()
        return obj_ret
    
    def __neg__(self):
        if self.denm<0:
            self.denm = -1*self.denm
            self.num = -1*self.num

        self.num = -1*self.num
        return self

    
class MVPoly():
    def __init__(self):
        self.variables = []
        self.terms = []
        self.coeffs = []
        self.z3_vars = None

    def reduce(self):
        uniq_terms = [list(i) for i in list(set([tuple(i) for i in self.terms]))]
        coeffs = []
        new_variables = self.variables.copy()

        #compute unique coefficients
        for i in range(0,len(uniq_terms)):
            curr_coeff = rational(0,1)
            for j in range(0,len(self.terms)):
                if uniq_terms[i] == self.terms[j]:
                    curr_coeff = curr_coeff + self.coeffs[j]
            coeffs.append(curr_coeff)
        
        #compute useless variables
        useless_vars = []
        for i in range(0,len(self.variables)):
            is_useful = False
            for j in uniq_terms:
                if j[i] > 0:
                    is_useful = True
                    break
            if is_useful==False:
                useless_vars.append(i)
        
        #remove indices corresponding to useless variables
        for i in range(len(useless_vars)-1,-1,-1):
            remove_index = useless_vars[i]
        
            for j in range(0,len(uniq_terms)):
                del uniq_terms[j][remove_index]
        
            del new_variables[remove_index]
        
        self.variables = new_variables
        self.coeffs = coeffs
        self.terms = uniq_terms


    def pretty_print(self):
        the_print_str = ""
        for i in range(0,len(self.coeffs)):
            if i != 0:
                the_print_str += " + "
            the_print_str += str(self.coeffs[i].num)+"/"+str(self.coeffs[i].denm)
            # the_print_str += "*"
            for j in range(0,len(self.terms[i])):
                if self.terms[i][j]>0:
                    the_print_str += "*"+str(self.variables[j])+"^"+str(self.terms[i][j])
        return the_print_str
    
    """

    def __add__(self, p):

        new_poly = MVPoly()
        new_poly.variables = self.variables + [i for i in p.variables if i not in self.variables]
        
        new_terms_count = len(new_poly.variables) - len(self.variables)

        terms = [i.copy()+[0 for _ in range(new_terms_count)] for i in self.terms]
        coeffs = [rational(i.num, i.denm) for i in self.coeffs]

        for i in range(0,p.terms):
            new_term = [0 for _ in range(new_terms_count)]
            for j in range(0,p.terms[i]):
                var_idx = new_poly.variables.index(p.variables[j])
                new_term[var_idx] = p.terms[i][j]
            terms.append(new_term)
            coeffs.append(p.coeffs[i])
        
        new_poly.terms = terms
        new_poly.coeffs = coeffs

        new_poly.reduce()
    
    """

    def return_univariate_poly(self):
        non_zero_pow_vars = set()
        for i in self.terms:
            for j in range(0,len(i)):
                if i[j]!=0:
                    non_zero_pow_vars.add(j)
        if len(non_zero_pow_vars) > 0:
            return None
        
        var_index_element = None
        for i in non_zero_pow_vars:
            var_index_element = i
        
        assert var_index_element!=None

        max_pow = max([max(i) for i in self.terms])
        uv_coeffs = [rational(0,1) for _ in range(0,max_pow+1)]
        
        for i in self.terms:
            uv_coeffs[i[var_index_element]]+=self.coeffs[i]
        
        return uv_coeffs


    def substitute_poly(self, variable, rational_point):
        variable_index = self.variables.index(variable)
        
        if variable not in self.variables:
            return
        
        for i in range(0,len(self.terms)):
            pow = self.terms[i][variable_index]
            for _ in range(pow):
                self.coeffs[i] *= rational_point
        
        for i in range(0,len(self.terms)):
            del self.terms[i][variable_index]

        del self.variables[variable_index]
        self.reduce()

        return


    def __str__(self):
        s = "{{" + ",".join(["\""+i+"\"" for i in self.variables]) + "},{"
        
        for i in self.terms:
            s+="{"+",".join([str(j) for j in i])+"}," 
        s = s[:-1]+"},{"

        s += ",".join(["{"+str(j.num)+","+str(j.denm)+"}" for j in self.coeffs])
        s+= "}}"
        return s

    def __repr__(self) -> str:
        return str(self)
    

    def convert_z3(self):

        #self.z3_vars 
        if self.z3_vars == None:
            self.z3_vars = []
            for i in self.variables:
                self.z3_vars.append(z3.Real(i))
        
        assert len(self.z3_vars) == len(self.variables)
        

        final_expr = z3.RealVal('0')

        # construct sum of all terms
        for i in range(0,len(self.terms)):

            #construct a particular term
            curr_expr = z3.RealVal(str(self.coeffs[i]))
            for j in range(0,len(self.terms[i])):
                pow = self.terms[i][j]
                for _ in range(pow):
                    curr_expr *= self.z3_vars[j]
            
            final_expr += curr_expr
        
        # returninng final expression
        return final_expr

    def copy_poly(self):
        p = MVPoly()
        p.variables = self.variables.copy()
        p.coeffs = [rational(i.num, i.denm) for i in self.coeffs]
        p.terms = [i.copy() for i in self.terms]
        return p
    
class MVPoly_constraint():    
    def __init__(self, poly=None, comparison=None):
        if poly == None:
            self.poly = MVPoly()
            self.comparison = -1
            return
        
        if comparison == None:
            self.poly = MVPoly()
            self.poly.terms = [i.copy() for i in poly.terms]
            self.poly.variables = poly.variables.copy()
            self.poly.coeffs = [rational(i.num, i.denm) for i in poly.coeffs]
            return 

        self.poly = MVPoly()
        self.poly.terms = [i.copy() for i in poly.terms]
        self.poly.variables = poly.variables.copy()
        self.poly.coeffs = [rational(i.num, i.denm) for i in poly.coeffs]
        self.comparison = comparison
    
    def __str__(self):
        t = str(self.poly)
        if self.comparison == LE:
            t += " <= 0"
        else:
            t+= " < 0"
        return t

    def __repr__(self) -> str:
        return str(self)


    def convert_z3(self):
        expr = self.poly.convert_z3()
        
        if self.comparison == LE:
            expr = (expr <= z3.RealVal("0"))
        else:
            expr = (expr < z3.RealVal("0"))
        
        return expr

    def copy_constraint(self):
        p = self.poly.copy_poly()
        comp = self.comparison
        constr = MVPoly_constraint(poly=p,comparison=comp)
        return constr


    def substitute_poly(self, variable, rational_point):
        poly = self.poly
        if variable not in poly.variables:
            return
        
        variable_index = poly.variables.index(variable)
        
        for i in range(0,len(poly.terms)):
            pow = poly.terms[i][variable_index]
            for _ in range(pow):
                poly.coeffs[i] *= rational_point
        
        for i in range(0,len(poly.terms)):
            del poly.terms[i][variable_index]

        del poly.variables[variable_index]
        poly.reduce()

        return


    def pretty_print(self):
        poly_pretty = self.poly.pretty_print()
        comparison_op = "<=" if self.comparison==LE else "<"
        return poly_pretty + " " + comparison_op + " 0"
    


def read_input_files(file_name):
    
    non_empty_lines = []
    
    with open(file_name, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
    for i in lines:
        #remove all spaces
        i = i.strip().replace(" ","")

        #remove empty lines
        if i!="":
            non_empty_lines.append(i)
    

    op_vars = non_empty_lines[0].split(":")[-1].split(",")
    # print(op_vars)
    # exit(-1)

    ip_vars = non_empty_lines[1].split(":")[-1].split(",")
    # print(ip_vars)
    # exit(-1)
    
    all_constraints = []
    i = 2
    while i<len(non_empty_lines):
        terms = non_empty_lines[i]
        i+=1
        
        coeffs = non_empty_lines[i]
        i+=1

        sign = non_empty_lines[i]
        i+=1


        coeffs_len = len("Coeffs:")
        
        terms = [i_.split(",") for i_ in terms.split(":")[1:]]
        terms = [[int(terms[j][k]) for k in range(len(terms[j]))] for j in range(len(terms))]
        # print(terms)
        # exit(-1)

        # coeffs = coeffs[coeffs_len:]
        coeffs = [i_.split(",") for i_ in coeffs.split(":")[1:]]
        coeffs = [rational(int(coeffs[j][0]),int(coeffs[j][1])) for j in range(len(coeffs))]
        # print(coeffs)
        # exit(-1)

        if sign == "<=":
            sign = LE
        else:
            sign = LT
        

        poly = MVPoly()
        #by convention the input first has output variables
        #   followed by input variables.
        poly.variables = op_vars + ip_vars
        poly.coeffs = coeffs
        poly.terms = terms

        constraint = MVPoly_constraint(poly=poly, comparison=sign)
        
        all_constraints.append(constraint)
    
    # for i in all_constraints:
    #     print(i.pretty_print())
    # exit(-1)
    # print(all_constraints)
    # exit(-1)
    return all_constraints, op_vars, ip_vars

def return_smt_file(input_file_name, output_file_name):
    all_constraints, op_vars, ip_vars = read_input_files(input_file_name)
    print(op_vars, ip_vars, all_constraints)
    #output and input variables in z3 format
    op_vars_z3 = [z3.Real(i) for i in op_vars]
    ip_vars_z3 = [z3.Real(i) for i in ip_vars]

    #converting the post condition in z3 format
    post_condition = [i.convert_z3() for i in all_constraints]

    #getting the post condition as a z3 formulae
    post_condition = z3.And(post_condition)
    solver = z3.Solver()
    solver.add(post_condition)
    smtlib_string = solver.to_smt2()
    # print(smtlib_string)
    with open(output_file_name, "w") as f:
        f.write(smtlib_string)
        f.write("\n")
    return op_vars, op_vars_z3, ip_vars, ip_vars_z3

if __name__ == "__main__":
    op, _, ip, _ = return_smt_file(sys.argv[1], sys.argv[2])

    with open(sys.argv[3], "w") as f:
        print(" ".join(ip), file=f, flush=True)
        print(" ".join(op), file=f, flush=True)