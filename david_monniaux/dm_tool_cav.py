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

sys.path.append("lib")
import convert_input_smt_format
import logging
import timeit
import argparse

# from typing import List


#the following converts from z3 sexpr to sympy and returns it
from smt_sympy_converter import sexpr_to_sympy

#the following converts from sympy to z3
from sympy_z3 import sympy_to_z3


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


def convert_string_rational(point):
    # print("A:",point)
    # print(type(point))
    
    # point = str(point)
    # if str(point) == "True":
    #     return "True"
    # elif str(point) == "False":
    #     return "False"
        
    assert ("/" in point) or (int(point)==float(point)),\
        "ERROR point returned by z3 is not rational"


    # point_tmp = rational(num=0,denm=0)
    if "/" in point:
        num = point.split("/")[0]
        denm = point.split("/")[1]
    else:
        num = int(point)
        denm = 1
    num = int(num)
    denm = int(denm)
    assert denm != 0, "Error: denominator = 0"
    return (num,denm)


#here pre_conditions will be [(pre-condition:pympy, op_variable_assignment_dict)]
def synthesize_program(file_name, pre_conditions, post_condition, ip_vars, op_vars, weakest_pre_condition=False):


    tmp = sys.stdout
    sys.stdout = open(file_name, "w+")

    # print("from helper_prog_python import *")
    print("import sympy")
    print("from sympy import *")

    #write pre_conditions
    for i in range(len(pre_conditions)):
        print()
        print("def pre_condition_"+str(i)+"(", end="")
        arguments = ",".join([ip_var+":sympy.Rational" for ip_var in ip_vars])
        print(arguments+"):")
        print("\t#"+str(pre_conditions[i][0]))
        
        print()
        print(f"\tpre_cond = {sympy.srepr(pre_conditions[i][0])}")
        # print("substitution = dict()")
        
        print()
        print(f"\teval = pre_cond.subs(",'{',", ".join(["\'"+i+"\':"+i for i in ip_vars]),'})')

        print()
        print(f"\tif eval==True:")
        print(f"\t\tassert eval!=False")
        print(f"\t\treturn True")
        print(f"\treturn False")
        print()

    
    #write a post-condition evaluation function just for logging, this function will not be used
    all_vars = ", ".join([f"{i}:sympy.Rational" for i in ip_vars+op_vars])
    
    print()
    print(f"def post_condition({all_vars}):")    

    print("\t#",str(post_condition))
    print()
    print("\tpost_cond = ",sympy.srepr(post_condition))
    print()
    print(f"\teval = post_cond.subs(",'{',", ".join(["\'"+i+"\':"+i for i in ip_vars+op_vars]),'})')

    print()
    print(f"\treturn eval == sympy.logic.boolalg.BooleanTrue")
    print()
    print()
    print()
    

    print()
    print()
    print("if __name__==\"__main__\":")
    print("\t", end="\n")

    #take input
    for i in ip_vars:
        print("\tip_0=int(input(\"enter integer numerator of "+i+":\\n\"))")
        print("\tip_1=int(input(\"enter integer denominator of "+i+":\\n\"))")
        print("\tassert(ip_1!=0), (\"Error denominator entered is 0\")")
        
        print("\t"+i+"=sympy.Rational(ip_0,ip_1)")
        print("\t")
        print("\t")

    for i in range(len(pre_conditions)):
        print("\t")
        print("\t")

        print("\tif pre_condition_"+str(i)+"("+",".join([ip_var+"="+ip_var for ip_var in ip_vars])+")==True:")
        print(f"\t\tprint(\"pre_condition_{i} SAT\")")
        
        op_eval_dict = pre_conditions[i][1]
        for j in op_eval_dict.keys():
            print(f"\t\tprint('{str(j)} = {op_eval_dict[j]}')")
        print("\t\texit(0)")


    print()
    print()
    if weakest_pre_condition:
        print("\tprint(\"Weakest pre-condition UNSAT\")", flush=True)
    else:
        print("\tprint(\"UNKNOWN\")", flush=True)
    print("\texit(0)")
    sys.stdout.close()
    sys.stdout = tmp
    # exit(-1)


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='NQS', usage='%(prog)s [-h] [options] post_condition', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ##  arguments
    parser.add_argument('post_condition', help='path to post_condition SMT file', metavar='post_condition')

    parser.add_argument('--ip_op_vars', help='path to input output variables file',type=str, default=None)
    
    parser.add_argument('--random_seed', help='random seed', type=int, default=10)
    
    parser.add_argument('--log_file', help='path to log file', type=str, default="dm_log.txt")

    parser.add_argument('--timer_log_file', help='path to timer log file', type=str, default="dm_timer_log.txt")
    
    parser.add_argument('--program_name', help='name of the program file', type=str, default="dm_program.py")
    
    

    args = parser.parse_args()
    
    log_file_name = args.log_file
    timer_logs_file = args.timer_log_file
    random_seed = args.random_seed
    ip_op_vars_file = args.ip_op_vars
    post_condition_file = args.post_condition
    op_program_file_name = args.program_name

    iteration_index = 0
    random.seed(random_seed)

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

        with open(ip_op_vars_file, "w+") as f:
            print(" ".join(ip_vars), file=f, flush=True)
            print(" ".join(op_vars),file=f, flush=True)

    else:

        want_ip_vars = []
        want_op_vars = []
        # if "zankl" in ip_file_name:
        #     want_ip_vars = ["b", "delta"]
        #     want_op_vars = ["a"]
        # if "asin_8_vars4" in ip_file_name:
        #     want_ip_vars = ["delta", "skoX", "skoS2"]
        #     want_op_vars = ["skoSP", "skoSM"]
        # if "asin_8_asin-8" in ip_file_name:
        #     want_ip_vars = ["delta", "skoX", "skoS2", "pi"]
        #     want_op_vars = ["skoSP","skoSM"]
        # if "Arthan_M2" in ip_file_name:
        #     want_ip_vars = ["delta", "skoSINS", "skoM"]
        #     want_op_vars = ["skoCOSS", "skoS"]
        # if "Arthan_KM2" in ip_file_name:
        #     want_ip_vars = ["delta", "skoS"]
        #     want_op_vars = ["skoCOSS","skoSINS"]
        # if "Arthan_1C" in ip_file_name\
        #     or "Arthan_1A" in ip_file_name:
        #     want_ip_vars = ["delta", "skoS","pi"]
        #     want_op_vars = ["skoCOSS","skoSINS"]
        ip_vars = want_ip_vars
        op_vars = want_op_vars

        # if len(want_op_vars + want_ip_vars) == 0:
        assert len(sys.argv) > 2, "need a file with ip/op variables"
        ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=input_output_variables_file_name)
        
        # assert len(sys.argv) > 2, "need a file with ip/op variables"
        # ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=input_output_variables_file_name)
    
    assert len(ip_vars + op_vars) == len(set(ip_vars+op_vars)), f"Repeating variables {ip_vars + op_vars}"

    # with open(log_file_name, "w+") as f:
    logger.debug(f"ip_vars: {ip_vars}")
    logger.debug(f"op_vars: {op_vars}")



    
    if "smt" in ip_file_name.split(".")[-1]:

        #read the post condition from the SMT file directly
        post_condition = z3.And(z3.parse_smt2_file(ip_file_name))
        sexpr_str = post_condition.sexpr()
        
        logger.debug(f"post_condition_smt:{post_condition}")

        # Convert post_condition to SymPy
        symbols_set, sympy_expr = sexpr_to_sympy(sexpr_str)

        post_condition_free_variables = [str(i) for i in sympy_expr.free_symbols]

        op_var_index = 0
        while op_var_index!=len(op_vars):
            if op_vars[op_var_index] not in post_condition_free_variables:
                del op_vars[op_var_index]
                op_var_index -= 1
            op_var_index += 1
        
        ip_var_index = 0
        while ip_var_index!=len(ip_vars):
            if ip_vars[ip_var_index] not in post_condition_free_variables:
                del ip_vars[ip_var_index]
                ip_var_index -= 1
            ip_var_index += 1
        
        logger.debug(f"POST_CONDITION_SYMPY: {sympy_expr}, {symbols_set}")
        print("POST_CONDITION:", sympy_expr)
        print("Input_Vars:", ip_vars)
        print("Output_Vars:", op_vars)
        assert len(op_vars) > 0, f"NO output variable in the post_condition {sympy_expr}"

        print("working...")
        # exit(-1)
        # print(symbols_set)
        # print(sympy_expr.free_symbols)
        symbols_sympy_dict = {str(i):i for i in sympy_expr.free_symbols}
        # print([type(i) for i in symbols_set])



        

        
        
        logger.debug(f"vars sympy:{([str(i) for i in sympy_expr.free_symbols])}")

        #get z3 expression completely
        vars_dict = dict()
        z3_expression = sympy_to_z3(sympy_expr, vars_dict)

        logger.debug(f"z3 vars:{vars_dict}")
        logger.debug(f"z3 post_condition:{z3_expression}")
        
        #create a solver and add the post-condition
        s = Solver()
        s.add(z3_expression)

        current_time = timeit.default_timer()
        with open(timer_logs_file,"w+") as f:
            print("TIME_Z3_START:", current_time, file=f, flush=True)
        
        is_solution = s.check()
        
        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_Z3_FINISH:", current_time, file=f, flush=True)
        
        
        if is_solution != z3.sat:
            print("exiting the code now...")
            print("post-condition unsat/z3 timeout no pre-condition generated!")
            print("no program generated!")
            exit(-1)
        
        pre_conditions = []

        while is_solution == z3.sat:
            logger.debug(f"---------point-synthesis-------------")
            
            m = s.model()
            
            is_solution_rational = True

            model_vals = []
            #check if all the declarations are good
            # print("decls:", m.decls())
            # print("vals:", [f"{var}="+str(m[avar]) for var,avar in vars_dict.items()])

            # exit(-1)
            for str_var, z3_var in vars_dict.items():

                try:
                    convert_rational = convert_string_rational(str(m[z3_var]))

                except:

                    logger.debug("IRRATIONAL")

                    logger.debug("model:"+", ".join([str(i)+"="+str(m[j]) for i,j in vars_dict.items()]))
                    
                    formula_new = z3.Or([j!=m[j] for i,j in vars_dict.items()])
                    
                    s.add(formula_new)

                    current_time = timeit.default_timer()
                    with open(timer_logs_file,"a") as f:
                        print("TIME_Z3_START:", current_time, file=f, flush=True)
                    
                    is_solution = s.check()

                    current_time = timeit.default_timer()
                    with open(timer_logs_file,"a") as f:
                        print("TIME_Z3_FINISH:", current_time, file=f, flush=True)

                    is_solution_rational = False
                    break
                
                model_vals.append((str_var,convert_rational))

            if is_solution_rational == False:

                with open(timer_logs_file,"a") as f:
                    print("IRRATIONAL_POINT", file=f, flush=True)

                continue
            else:
                rat_point = ", ".join([str(i)+"="+str(m[j]) for i,j in vars_dict.items()])
                logger.debug(f"RATIONAL point: {rat_point}")
                with open(timer_logs_file,"a") as f:
                    print("RATIONAL_POINT", file=f, flush=True)

            
            # print("MODEL_VALS:", model_vals)
            sympy_vals = {i[0]: sympy.Rational(i[1][0],i[1][1]) for i in model_vals}
            

            substitution = dict()
            for i in range(len(op_vars)):
                op_var = op_vars[i]
                substitution[symbols_sympy_dict[op_var]] = sympy_vals[op_var]
                logger.debug(f"---------pre-condition {iteration_index}---------")
            
                # print(substitution)
                # print(sympy_expr)
                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_SUBS_SIMPLIFY_START:", current_time, file=f, flush=True)
                
                sub_expr = sympy_expr.subs(substitution)

                # print(sub_expr)
                sub_expr =  sub_expr.simplify()
                # print(sub_expr)
                # print("______________")
                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_SUBS_SIMPLIFY_STOP:", current_time, file=f, flush=True)
                
                sympy_pre_cond = sub_expr


                iteration_index+=1



                logger.debug(f"PRECOND_{iteration_index-1}: {sympy_pre_cond}")


                pre_conditions.append((sympy_pre_cond.copy(), sympy_vals.copy()))

                pre_cond_z3 = sympy_to_z3(sympy_pre_cond, vars_dict)
                
                s.add(z3.Not(pre_cond_z3))
                
                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_PROG_SYN_START:", current_time, file=f, flush=True)

                synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr,ip_vars=ip_vars,op_vars=op_vars)

                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_PROG_SYN_STOP:", current_time, file=f, flush=True)
                # exit(-1)
            # print()
            # print(s)
            # print()
            
            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_Z3_START:", current_time, file=f, flush=True)
            is_solution = s.check()
            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_Z3_FINISH:", current_time, file=f, flush=True)

            # print("SYMPY_VALS:", sympy_vals)
            
            # exit(-1)

        print()
        print("IS_SOLUTION:", is_solution)
        # print()
        if is_solution == z3.unsat:

            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_PROG_SYN_START:", current_time, file=f, flush=True)
            synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr,ip_vars=ip_vars,op_vars=op_vars, weakest_pre_condition=True)

            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_PROG_SYN_STOP:", current_time, file=f, flush=True)
            with open(timer_logs_file, "a") as f:
                print("WEAKEST_PRE_COND_SYNTHESIZED", file=f, flush=True)
            print("WEAKEST_PRE_COND_SYNTHESIZED")
            logger.debug("WEAKEST_PRE_COND_SYNTHESIZED")
            for i,j in pre_conditions:
                print(i, ",", j)
                logger.debug(f"{i} {j}")

        else:
            assert is_solution == z3.unknown, {is_solution}
            with open(timer_logs_file, "a") as f:
                print("ERROR_UNKNOWN_TERMINATION", file=f, flush=True)
            synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr,ip_vars=ip_vars,op_vars=op_vars, weakest_pre_condition=True)
            print("ERROR_UNKNOWN_TERMINATION")
            logger.debug("ERROR_UNKNOWN_TERMINATION")
            for i,j in pre_conditions:
                print(i, ",", j)
                logger.debug(f"{i} {j}")
