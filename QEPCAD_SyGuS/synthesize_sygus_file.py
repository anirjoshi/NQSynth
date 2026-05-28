#./execute_all_smt_small_benchmarks.sh examples/small_smt_files/ log_file_smt
#./execute_all_smt_small_benchmarks.sh examples/small_smt_files/ log_file_smt
#cvc5 --sygus-qe-preproc --lang=sygus2 tmp.sy

import os
import sys
import math
import z3
import logging
import random
import yaml
import argparse
import re

from z3 import *



def fetch_input_output_variables(input_output_variables_file_path):
    with open(input_output_variables_file_path, "r") as ip_op_file:
        ip_op_lines = ip_op_file.readlines()
    
    ip_vars = []
    op_vars = []
    ip_lines = False
    op_lines = False
    for line in ip_op_lines.copy():
        line = re.sub(r'\s+', '', line.strip())
        if "input" in line.split(":")[0].lower() or\
            "ip" in line.split(":")[0].lower():
            ip_vars = line.split(":")[1].replace(" ","").split(",")
            ip_lines = True
        if "output" in line.split(":")[0].lower() or\
            "op" in line.split(":")[0].lower():
            op_vars = line.split(":")[1].replace(" ","").split(",")
            op_lines = True
    if not(ip_lines):
        if "," in ip_op_lines[0]:
            line = re.sub(r'\s+', '', ip_op_lines[0].strip())
            ip_vars = line.split(",")
        else:
            ip_vars = ip_op_lines[0].split()


    if not(op_lines):
        if "," in ip_op_lines[1]:
            line = re.sub(r'\s+', '', ip_op_lines[1].strip())
            op_vars = line.split(",")
        else:
            op_vars = ip_op_lines[1].split()

    
    assert len(ip_vars+op_vars) == len(set(ip_vars+op_vars)), f"common variables between inputs:{ip_vars} and outputs:{op_vars}"
    return ip_vars, op_vars




class AstRefKey:
    def __init__(self, n):
        self.n = n
    def __hash__(self):
        return self.n.hash()
    def __eq__(self, other):
        return self.n.eq(other.n)
    def __repr__(self):
        return str(self.n)

def askey(n):
    assert isinstance(n, z3.AstRef)
    return AstRefKey(n)

def get_vars(f):
    r = []
    t = []
    var = []
    def collect(f):
        if z3.is_const(f): 
            if f.decl().kind() == z3.Z3_OP_UNINTERPRETED and not askey(f) in r:
                var.append(f.decl())
                r.append(askey(f))
                t.append(f.sort())
        else:
            for c in f.children():
                collect(c)
    collect(f)
    return r,t




def synthesize_sygus_file(post_condition_file, pre_condition_file, ip_vars, op_vars, output_file, pre_condition_z3_sexpr=None):
    
    if pre_condition_z3_sexpr == None:
        pre_conditions = z3.And(z3.parse_smt2_file(pre_condition_file))
        pre_condition_sexpr = pre_conditions.sexpr()
        # print("pre_conditionsexpr:", pre_condition_sexpr, pre_conditions,z3.parse_smt2_file(pre_condition_file).sexpr())
    else:
        pre_condition_sexpr = pre_condition_z3_sexpr

    post_condition = z3.And(z3.parse_smt2_file(post_condition_file))
    post_condition_sexpr = post_condition.sexpr()
    
    f = open(output_file, 'w')
    curr_stdout = sys.stdout
    sys.stdout = f

    print("(set-logic NRA)")
    
    
    for op_var in op_vars:
        op_var_fun = op_var+"_o"
        dec_function = op_var_fun+" ( "
        arguments = " ".join(["( "+ip_var+"_i Real )" for ip_var in ip_vars])
        dec_function += arguments
        dec_function += " ) Real"
        dec_function = "(synth-fun "+dec_function+" )"
        print(dec_function)

        arguments_substitute = " ".join(ip_vars)
        # print("AAA:", post_condition_sexpr)
        # print("AAAV:", m)
        # print("AAAc:", post_condition_sexpr)
        post_condition_sexpr = post_condition_sexpr.replace("\n"," ")
        
        # for tmp in range(len(m)):
        #     if len(m[tmp])>= len(op_var)\
        #         and m[tmp][-len(op_var):] == op_var:
        #         if len(m[tmp])>len(op_var) and\
        #         (m[-(len(op_var)+1)]==" "):
        #             m[tmp] = m[tmp][:-len(op_var)]+f"({op_var} {arguments_substitute})"
        #         else:
        #             m[tmp] = m[tmp][:-len(op_var)]+f"({op_var} {arguments_substitute})"
        # m = " ".join(m)
        # post_condition_sexpr = m
        post_condition_sexpr_b = None
        while (post_condition_sexpr_b != post_condition_sexpr):

            post_condition_sexpr_b = post_condition_sexpr

            match1 = " "+op_var+" "
            replace1 = " "+f"({op_var_fun} {arguments_substitute})"+" "
            # print("A:", post_condition_sexpr, op_var)
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            # print("AR:", post_condition_sexpr)

            match1 = " "+op_var+"("
            replace1 = " "+f"({op_var_fun} {arguments_substitute})"+" ("
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = " "+op_var+")"
            replace1 = " "+f"({op_var_fun} {arguments_substitute})"+" )"
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = "("+op_var+" "
            replace1 = "( "+f"({op_var_fun} {arguments_substitute})"+" "
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = "("+op_var+"("
            replace1 = "( "+f"({op_var_fun} {arguments_substitute})"+" ("
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = "("+op_var+")"
            replace1 = "( "+f"({op_var_fun} {arguments_substitute})"+" )"
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = ")"+op_var+" "
            replace1 = ") "+f"({op_var_fun} {arguments_substitute})"+" "
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = ")"+op_var+"("
            replace1 = ") "+f"({op_var_fun} {arguments_substitute})"+" ("
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = ")"+op_var+")"
            replace1 = ") "+f"({op_var_fun} {arguments_substitute})"+" )"
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
        

                  
        # post_condition_sexpr = post_condition_sexpr.replace(op_var,f"({op_var} {arguments_substitute})")
    

    for ip_var in ip_vars:
        dec_var = "(declare-var "+ip_var+" Real)"
        print(dec_var)


    # print(post_condition_sexpr)
    
    print(f"( constraint (=> {pre_condition_sexpr} {post_condition_sexpr}))")
    print("( check-synth )")
    print("(exit)")

    sys.stdout = curr_stdout
    f.close()
    return





if __name__ == "__main__":
    #print system arguments
    print(sys.argv)

    #input files:
    #config.txt

    
    parser = argparse.ArgumentParser(description='Syntheize SyGuS', usage='%(prog)s [-h] [options] post_condition ip_op_vars pre_condition', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ##  arguments
    parser.add_argument('post_condition', help='path to post_condition SMT file', metavar='post_condition')


    parser.add_argument('ip_op_vars', help='path to input output variables file',type=str, default=None, metavar='ip_op_vars')
    
    parser.add_argument('pre_condition', help='path to post_condition SMT file', type=str, metavar="post_condition")


    parser.add_argument('--output_file', help='path to output file', type=str, default="sygus.sy")


    args = parser.parse_args()
    

    post_condition_smt_file = args.post_condition
    # prog_syn_data = "prog_syn_data.txt"
    pre_conditions_smt_file = args.pre_condition
    ip_op_vars_file = args.ip_op_vars
    sygus_file_name = args.output_file

    # print(post_condition_smt_file, prog_syn_data, pre_conditions_smt_file,ip_op_vars_file)
    ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=ip_op_vars_file)
    # with open(ip_op_vars_file, "r") as f:
    #     all_lines = f.readlines()
    #     ip_vars = all_lines[0].strip().split()
    #     op_vars = all_lines[1].strip().split()
    
    print(ip_vars, op_vars)

    pre_conditions = z3.And(z3.parse_smt2_file(pre_conditions_smt_file))
    pre_condition_sexpr = pre_conditions.sexpr()
    
    post_condition = z3.And(z3.parse_smt2_file(post_condition_smt_file))
    post_condition_sexpr = post_condition.sexpr()
    
    f = open(sygus_file_name, 'w')
    curr_stdout = sys.stdout
    sys.stdout = f

    print("(set-logic NRA)")
    
    
    for op_var in op_vars:
        op_var_fun = op_var+"_o"
        dec_function = op_var_fun+" ( "
        arguments = " ".join(["( "+ip_var+"_i Real )" for ip_var in ip_vars])
        dec_function += arguments
        dec_function += " ) Real"
        dec_function = "(synth-fun "+dec_function+" )"
        print(dec_function)

        arguments_substitute = " ".join(ip_vars)
        # print("AAA:", post_condition_sexpr)
        # print("AAAV:", m)
        # print("AAAc:", post_condition_sexpr)
        post_condition_sexpr = post_condition_sexpr.replace("\n"," ")
        
        # for tmp in range(len(m)):
        #     if len(m[tmp])>= len(op_var)\
        #         and m[tmp][-len(op_var):] == op_var:
        #         if len(m[tmp])>len(op_var) and\
        #         (m[-(len(op_var)+1)]==" "):
        #             m[tmp] = m[tmp][:-len(op_var)]+f"({op_var} {arguments_substitute})"
        #         else:
        #             m[tmp] = m[tmp][:-len(op_var)]+f"({op_var} {arguments_substitute})"
        # m = " ".join(m)
        # post_condition_sexpr = m
        post_condition_sexpr_b = None
        while (post_condition_sexpr_b != post_condition_sexpr):

            post_condition_sexpr_b = post_condition_sexpr

            match1 = " "+op_var+" "
            replace1 = " "+f"({op_var_fun} {arguments_substitute})"+" "
            # print("A:", post_condition_sexpr, op_var)
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            # print("AR:", post_condition_sexpr)

            match1 = " "+op_var+"("
            replace1 = " "+f"({op_var_fun} {arguments_substitute})"+" ("
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = " "+op_var+")"
            replace1 = " "+f"({op_var_fun} {arguments_substitute})"+" )"
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = "("+op_var+" "
            replace1 = "( "+f"({op_var_fun} {arguments_substitute})"+" "
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = "("+op_var+"("
            replace1 = "( "+f"({op_var_fun} {arguments_substitute})"+" ("
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = "("+op_var+")"
            replace1 = "( "+f"({op_var_fun} {arguments_substitute})"+" )"
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = ")"+op_var+" "
            replace1 = ") "+f"({op_var_fun} {arguments_substitute})"+" "
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = ")"+op_var+"("
            replace1 = ") "+f"({op_var_fun} {arguments_substitute})"+" ("
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
            

            match1 = ")"+op_var+")"
            replace1 = ") "+f"({op_var_fun} {arguments_substitute})"+" )"
            post_condition_sexpr = post_condition_sexpr.replace(match1, replace1)
        

                  
        # post_condition_sexpr = post_condition_sexpr.replace(op_var,f"({op_var} {arguments_substitute})")
    

    for ip_var in ip_vars:
        dec_var = "(declare-var "+ip_var+" Real)"
        print(dec_var)


    # print(post_condition_sexpr)
    
    print(f"( constraint (=> {pre_condition_sexpr} {post_condition_sexpr}))")
    print("( check-synth )")
    print("(exit)")

    sys.stdout = curr_stdout
    f.close()
