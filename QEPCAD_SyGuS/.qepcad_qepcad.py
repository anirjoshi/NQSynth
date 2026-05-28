import os
import sys
import math
import z3
import logging
import random
import re
import yaml
from datetime import datetime
from z3 import *
import time
import sympy
import logging
import timeit
import argparse
import synthesize_sygus_file

# from typing import List
sys.path.append("lib")

#convert the other input format to smt
import convert_input_smt_format

#the following converts from z3 sexpr to sympy and returns it
from smt_sympy_converter import sexpr_to_sympy

#the following converts from sympy to z3
from sympy_z3 import sympy_to_z3

from sympy_qepcad import convert_sympy_to_qepcad

from qepcad_sympy import sage_to_sympy2

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



def write_sage_file(sage_expr, vars_quantify_out, all_vars, sage_file):
    with open(sage_file, "w+") as f:
        tmp = sys.stdout
        sys.stdout = f

        for var in all_vars:
            print(f"var('{var}')")
        print("qf = qepcad_formula")
        print(f"F = {sage_expr}")
        print(f"E = qf.exists({vars_quantify_out},F)")
        print("print(qepcad(E, memcells='1000000000 +L5000'))")
        print("",flush=True)

        sys.stdout = tmp
    return



if __name__=="__main__":

    parser = argparse.ArgumentParser(description='stage2', usage='%(prog)s [-h] [options] post_condition ip_op_vars', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ##  arguments
    parser.add_argument('post_condition', help='path to post_condition SMT file', metavar='post_condition')

    parser.add_argument('ip_op_vars', help='path to input output variables file',type=str, default=None, metavar='ip_op_vars')

    parser.add_argument('pre_condition', help='path to pre_condition output SMT file', metavar='pre_condition')

    parser.add_argument('--sage_command', help='command to run a sage file', type=str, default="sage")

    parser.add_argument('--log_file', help='path to log file', type=str, default="gus_log.txt")

    parser.add_argument('--timer_log_file', help='path to timer log file', type=str, default="gus_timer_log.txt")

    parser.add_argument('--sage_dir', help='directory name for the location of all synthesized sage files', type=str, default="gus_sage_files")

    parser.add_argument('--output_sygus_file', help='path to output file', type=str, default="sygus.sy")

    

    args = parser.parse_args()
    
    command_run_sage_file = args.sage_command
    log_file_name = args.log_file
    timer_logs_file = args.timer_log_file
    sage_file_dir = args.sage_dir
    random_seed = 10
    ip_op_vars_file = args.ip_op_vars
    post_condition_file = args.post_condition
    pre_condition_file = args.pre_condition
    output_sygus_file = args.output_sygus_file
    
    random.seed(random_seed)

    # ip_file_name = sys.argv[1]
    # if len(sys.argv) > 2:
        # input_output_variables_file_name = sys.argv[2]
    ip_file_name = post_condition_file
    input_output_variables_file_name = ip_op_vars_file
    
    #remove the log_file if it exists
    os.system(f"rm {log_file_name}")
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
    logger.debug(f'Starting Log File: {log_file_name}')
    logger.info("")
    logger.info(f"input_file_name: {ip_file_name}")


    if "smt" not in ip_file_name.split(".")[-1]:

        output_file_name = ".".join(ip_file_name.split(".")[:-1])+".smt2"

        op_vars_, op_vars_z3_, ip_vars_, ip_vars_z3_ = convert_input_smt_format.return_smt_file(input_file_name=ip_file_name, output_file_name=output_file_name)
        ip_file_name = output_file_name
        
        ip_vars = ip_vars_
        op_vars = op_vars_
    
    else:    
        assert len(sys.argv) > 2, "need a file with ip/op variables"
        ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=input_output_variables_file_name)
    
    assert len(ip_vars + op_vars) == len(set(ip_vars+op_vars)), f"Repeating variables {ip_vars + op_vars}"

    # with open(log_file_name, "w+") as f:
    logger.debug(f"ip_vars: {ip_vars}")
    logger.debug(f"op_vars: {op_vars}")

    
    try:
        os.makedirs(sage_file_dir)
    except:
        pass
    os.system(f"rm {sage_file_dir}/*")



    
    if "smt" in ip_file_name.split(".")[-1]:

        #read the post condition from the SMT file directly
        post_condition = z3.And(z3.parse_smt2_file(ip_file_name))
        sexpr_str = post_condition.sexpr()
        
        logger.debug(f"post_condition_smt:{post_condition}")

        # Convert post_condition to SymPy
        symbols_set, sympy_expr = sexpr_to_sympy(sexpr_str)

        logger.debug(f"POST_CONDITION_SYMPY: {sympy_expr}, {symbols_set}")
        print("POST_CONDITION:", sympy_expr)
        print("Input_Vars:", ip_vars)
        print("Output_Vars:", op_vars)
        print("working...")
        # exit(-1)
        # print(symbols_set)
        # print(sympy_expr.free_symbols)
        symbols_sympy_dict = {str(i):i for i in sympy_expr.free_symbols}
        # print([type(i) for i in symbols_set])
        
        
        logger.debug(f"vars sympy:{([str(i) for i in sympy_expr.free_symbols])}")

        #get z3 expression completely
        # vars_dict = dict()
        # z3_expression = sympy_to_z3(sympy_expr, vars_dict)

        # logger.debug(f"z3 vars:{vars_dict}")
        # logger.debug(f"z3 post_condition:{z3_expression}")
        
        
        
        post_cond_sympy_expr = sympy_expr.simplify() 

        sage_expr = convert_sympy_to_qepcad(sympy.srepr(post_cond_sympy_expr))
        # print(sage_expr)

        sage_file = f"{sage_file_dir}/sage.sage"
        out_file = f"{sage_file_dir}/sage_output.txt"
                
        write_sage_file(sage_expr=sage_expr,vars_quantify_out=op_vars,all_vars=ip_vars+op_vars,sage_file=sage_file)
                
        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_SAGE_START:", current_time, file=f, flush=True)

        os.system(f"{command_run_sage_file} {sage_file} > {out_file}")
                
        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_SAGE_FINISH:", current_time, file=f, flush=True)
                
        with open(out_file,"r") as f:
            pre_cond = f.readlines()
            pre_cond = [i.strip() for i in pre_cond]
            pre_cond = " ".join(pre_cond)
            pre_cond = re.sub(r'\s+', ' ', pre_cond)
                
        logger.debug(f"WEAKEST_PRECOND: {pre_cond}")

        tmp = sys.stdout
        sys.stdout = sys.stdout = open(os.devnull, 'w')
        sympy_pre_cond = sage_to_sympy2(pre_cond)
        sys.stdout = tmp

        weakest_pre_condition = sympy_pre_cond.simplify().copy()

        vars_dict = dict()
        pre_cond_z3 = sympy_to_z3(sympy_pre_cond, vars_dict)

        print("pre_condition:", pre_cond_z3, type(pre_cond_z3))
        print("vars_dict:", vars_dict)

        s = Solver()
        s.add(pre_cond_z3)
        smt2_data = s.to_smt2()
        # smt2_data = pre_cond_z3.to_smt2()
        with open(pre_condition_file, "w") as f:
            print(smt2_data, file=f, flush=True)
            print("",file=f, flush=True)
        # current_time = timeit.default_timer()
        # with open(timer_logs_file,"a") as f:
        #     print("TIME_Z3_START:", current_time, file=f, flush=True)
        # current_time = timeit.default_timer()
        # with open(timer_logs_file,"a") as f:
        #     print("TIME_Z3_FINISH:", current_time, file=f, flush=True)


    print(f"synthesizing sygus file {output_sygus_file}....")
    synthesize_sygus_file.synthesize_sygus_file(post_condition_file=post_condition_file, pre_condition_file=pre_condition_file, ip_vars=ip_vars, op_vars=op_vars, output_file=output_sygus_file)
    
