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

# from typing import List
sys.path.append("lib")

try:
    sys.path.append('../lib')
except:
    pass

#convert the second input into smt format
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

def write_sage_file(sage_expr, var_quantify_out, all_vars, sage_file):
    with open(sage_file, "w+") as f:
        tmp = sys.stdout
        sys.stdout = f

        for var in all_vars:
            print(f"var('{var}')")
        print(f"var('{var_quantify_out}')")
        print("qf = qepcad_formula")
        print(f"F = {sage_expr}")
        print(f"E = qf.exists([{var_quantify_out}],F)")
        print("print(qepcad(E, memcells='1000000000 +L5000'))")
        print("",flush=True)

        sys.stdout = tmp
    return

import random
def sample_rational():
    # Random numerator and denominator
    numerator = random.randint(0, 1000)  # Random numerator
    denominator = random.randint(1, 1000)  # Random denominator, non-zero
    
    # Ensure it's between 0 and 1
    if numerator > denominator:
        numerator, denominator = denominator, numerator
    
    return (numerator, denominator)



def synthesize_program(file_name, pre_conditions, post_condition, ip_vars, op_vars, lambda_var, weakest_pre_condition=False):

    assert len(direction) == len(op_vars)
    tmp = sys.stdout
    sys.stdout = open(file_name, "w+")

    # print("from helper_prog_python import *")
    print("import sympy")
    print("from sympy import *")
    print("from NQS.helper_program_cav import get_lambda_val")
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
        # print(f"\treturn eval == sympy.logic.boolalg.BooleanTrue")
        
        # string_op = convert_string_to_if_condition(pre_conditions[i])

        # string_op = string_op.replace("/=","!=").replace(r"\=","!=").replace("\\=","!=")
        # string_op = string_op.replace("TRUE","True")
        # string_op = string_op.replace("FALSE", "False")

        # curr_stdout = sys.stdout
        # sys.stdout = f
        
        # print("\t")
        # print("\t#evaluate_pre_condition")
        # print("\tvalue = "+string_op)
        # print("\treturn value")
        # print()
    
    #write a post-condition evaluation function
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
    
    print("#return post-condition single variable")
    arguments = ", ".join(["post_condition"]+[i+":sympy.Rational=None" for i in ip_vars+op_vars])
    print(f"def return_post_condition_single_var({arguments}):") 
    for i in ip_vars:
        print(f"\tassert {i}!=None")
    print()  

    
    for i in op_vars:
        print()
        print(f"\tif {i}==None:")
        for j in op_vars:
            if j!=i:
                print(f"\t\tassert {j}!=None")
        arguments_str = ", ".join([j+"="+j for j in ip_vars+op_vars])
        print(f"\t\treturn lambda {i}: post_condition({arguments_str})")
    
    print()
    print()
    arguments_str = ", ".join([j+"="+j for j in ip_vars+op_vars])
    print(f"\treturn post_condition({arguments_str})")

    print()
    print()
    print(f"def get_univariate_poly(",", ".join([j+":sympy.Rational" for j in ip_vars+op_vars]),"):")
    print()
    print()
    print("\tpost_cond = ",sympy.srepr(post_condition))
    print()
    print(f"\teval = post_cond.subs(",'{',", ".join(["\'"+i+"\':"+i for i in ip_vars+op_vars]),'})')
    print(f"\treturn eval")
    print()
    




    print()
    print()
    print("if __name__==\"__main__\":")
    print("\t", end="\n")

    #take input
    for i in ip_vars:
        print("\tip_0=int(input(\"enter numerator of "+i+":\\n\"))")
        print("\tip_1=int(input(\"enter denominator of "+i+":\\n\"))")
        print("\tassert(ip_1!=0), (\"Error denominator entered is 0\")")
        
        print("\t"+i+"=sympy.Rational(ip_0,ip_1)")
        print("\t")
        print("\t")

    print(f"\t{lambda_var} = sympy.symbols('{lambda_var}')")

    for i in range(len(pre_conditions)):
        print("\t")
        print("\t")

        print("\tif pre_condition_"+str(i)+"("+",".join([ip_var+"="+ip_var for ip_var in ip_vars])+")==True:")


        print("\t\tall_vals = dict()")
        for j in ip_vars:
            print(f"\t\tall_vals['{j}'] = {j}")
        
        op_eval_dict = pre_conditions[i][2]
        for j in op_eval_dict.keys():
            print(f"\t\tall_vals['{str(j)}'] = {sympy.srepr(op_eval_dict[j])}")
        print("\t\tuv_poly_expr = get_univariate_poly(**all_vals)")
        print("\t\tsolution_exists,  lambda_val = get_lambda_val(uv_poly_expr)")
        print()
        print(f"\t\tif solution_exists:")
        print(f"\t\t\tprint(\"pre_condition_{i} SAT\")")
        for i in op_vars:
            print()
            print(f"\t\t\tprint(\"{i}=\", all_vals[\"{i}\"].subs(",'{',f"'{lambda_var}':lambda_val",'}',"))")
        print()
        print()
        print("\t\t\texit(0)")
        print("\t\tpass")

    print()
    print()
    if weakest_pre_condition==False:
        print("\tprint(\"UNKNOWN\")", flush=True)
    else:
        print("\tprint(\"Weakest pre-condition UNSAT\")", flush=True)
    sys.stdout.close()
    sys.stdout = tmp
    # exit(-1)


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='NQS', usage='%(prog)s [-h] [options] post_condition', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ##  arguments
    parser.add_argument('post_condition', help='path to post_condition SMT file', metavar='post_condition')

    parser.add_argument('--ip_op_vars', help='path to input output variables file',type=str, default="ip_op_vars.txt")
    
    parser.add_argument('--random_seed', help='random seed', type=int, default=10)
    
    parser.add_argument('--sage_command', help='command to run a sage file', type=str, default="sage")

    parser.add_argument('--log_file', help='path to log file', type=str, default="log.txt")

    parser.add_argument('--timer_log_file', help='path to timer log file', type=str, default="timer_log.txt")

    parser.add_argument('--sage_dir', help='directory name for the location of all synthesized sage files', type=str, default="sage_files")
    
    parser.add_argument('--program_name', help='name of the program file', type=str, default="program.py")


    args = parser.parse_args()
    
    post_condition_file = args.post_condition
    ip_op_vars_file = args.ip_op_vars
    random_seed = args.random_seed
    command_run_sage_file = args.sage_command
    log_file_name = args.log_file
    timer_logs_file = args.timer_log_file
    sage_file_dir = args.sage_dir
    op_program_file_name = args.program_name

    # command_run_sage_file = "sage"
    # log_file_name = "log.txt"
    # timer_logs_file = "timer_log.txt"
    # sage_file_dir = "sage_files/"
    # random_seed = 10 #None

    iteration_index = 0
    lambda_var_prefix = "lambda_var"
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

    assert "smt" in ip_file_name.split(".")[-1], f"Error: {ip_file_name} is not smt file"

    if False and "smt" not in ip_file_name.split(".")[-1]:
        #UNREACHABLE CODE
        output_file_name = ".".join(ip_file_name.split(".")[:-1])+".smt2"

        op_vars_, op_vars_z3_, ip_vars_, ip_vars_z3_ = convert_input_smt_format.return_smt_file(input_file_name=ip_file_name, output_file_name=output_file_name)
        ip_file_name = output_file_name
        
        ip_vars = ip_vars_
        op_vars = op_vars_
    
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

        if len(want_op_vars + want_ip_vars) == 0:
            assert len(sys.argv) > 2, "need a file with ip/op variables"
            ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=input_output_variables_file_name)
        else:
            with open(ip_op_vars_file, "w+") as f:
                print(" ".join(ip_vars), file=f, flush=True)
                print(" ".join(op_vars),file=f, flush=True)
      
        # assert len(sys.argv) > 2, "need a file with ip/op variables"
        # ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=input_output_variables_file_name)
    
    assert len(ip_vars + op_vars) == len(set(ip_vars+op_vars)), f"Repeating variables {ip_vars + op_vars}"

    # with open(log_file_name, "w+") as f:
    logger.debug(f"ip_vars: {ip_vars}")
    logger.debug(f"op_vars: {op_vars}")

    # create a new_lambda rational variable
    # lambda_var_prefix = "lambda_var"
    tmp_lambda_index = 0
    lambda_var = lambda_var_prefix + "_" + str(tmp_lambda_index)
    while lambda_var in ip_vars + op_vars:
        tmp_lambda_index += 1
        lambda_var = lambda_var_prefix + "_" + str(tmp_lambda_index)
    
    #log the lambda_var
    logger.debug(f"lambda_var: {lambda_var}")

    sympy_lambda_var = sympy.symbols(lambda_var)

    assert lambda_var not in ip_vars+op_vars, f"lambda_var={lambda_var} in {ip_vars+op_vars}"

    directions = [[sympy.Rational(0,1) if j!=i else sympy.Rational(1,1) for j in range(len(op_vars))] for i in range(len(op_vars))]

    # new_directions = [[sympy.Rational(*sample_rational()) for _ in range(len(op_vars))] for _ in range(10)]
    # directions = directions + new_directions
    
    #log the directions
    logger.debug(f"DIRECTIONS: {len(directions)}:{directions}")
    
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
            logger.debug("")
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
                logger.debug(f"RATIONAL point:, {rat_point}")
                with open(timer_logs_file,"a") as f:
                    print("RATIONAL_POINT", file=f, flush=True)

            
            # print("MODEL_VALS:", model_vals)
            sympy_vals = {i[0]: sympy.Rational(i[1][0],i[1][1]) for i in model_vals}

            

            for direction in directions:
                substitution = dict()
                for i in range(len(op_vars)):
                    op_var = op_vars[i]
                    if op_var not in symbols_sympy_dict.keys():
                        new_symbol =sympy.symbols(op_var)
                        substitution[new_symbol] = sympy.Rational(0,1) + sympy_lambda_var*direction[i]    
                    else:
                        substitution[symbols_sympy_dict[op_var]] = sympy_vals[op_var] + sympy_lambda_var*direction[i]
                logger.debug(f"---------pre-condition {iteration_index}---------")
                logger.debug(f"direction: {direction}")
                logger.debug(f"substitution: {substitution}")
            
                # print(substitution)
                # print(sympy_expr)
                sub_expr = sympy_expr.subs(substitution)

            
                sub_expr =  sub_expr.simplify()
                # print(sub_expr)
        
                sage_expr = convert_sympy_to_qepcad(sympy.srepr(sub_expr))
                # print(sage_expr)

                sage_file = f"{sage_file_dir}/sage_{iteration_index}.sage"
                out_file = f"{sage_file_dir}/sage_output_{iteration_index}.txt"
                
                print(sub_expr.free_symbols)
                print(lambda_var)

                
                write_sage_file(sage_expr=sage_expr,var_quantify_out=lambda_var,all_vars=ip_vars+op_vars,sage_file=sage_file)
                
                if str(lambda_var) in [str(m) for m in sub_expr.free_symbols]:
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

                    logger.debug(f"PRECOND_{iteration_index-1}: {pre_cond}")

                    tmp = sys.stdout
                    sys.stdout = sys.stdout = open(os.devnull, 'w')
                    sympy_pre_cond = sage_to_sympy2(pre_cond)
                    sys.stdout = tmp

                else:
                    current_time = timeit.default_timer()
                    with open(timer_logs_file,"a") as f:
                        print("TIME_SAGE_START:", current_time, file=f, flush=True)
                        print("TIME_SAGE_FINISH:", current_time, file=f, flush=True)
                    pre_cond = sub_expr
                    logger.debug(f"PRECOND_{iteration_index-1}: {pre_cond}")
                    sympy_pre_cond = sub_expr
                    pre_cond = None
                    sub_expr = None
                
                iteration_index+=1

                

                # print(sympy_pre_cond)

                pre_conditions.append((sympy_pre_cond.copy(), sympy_vals.copy(), substitution.copy()))

                pre_cond_z3 = sympy_to_z3(sympy_pre_cond, vars_dict)
                
                s.add(z3.Not(pre_cond_z3))
                # exit(-1)
                # print("_______________________________")
                # for i in pre_conditions:
                #     print(i)
                # print("_______________________________")
                synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr,ip_vars=ip_vars,op_vars=op_vars, lambda_var=lambda_var)
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
        # print()
        if is_solution == z3.unsat:
            synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr,ip_vars=ip_vars,op_vars=op_vars, lambda_var=lambda_var, weakest_pre_condition=True)
            print("WEAKEST_PRE_COND_SYNTHESIZED")
            with open(timer_logs_file, "a") as f:
                print("WEAKEST_PRE_COND_SYNTHESIZED", file=f, flush=True)
            logger.debug("WEAKEST_PRE_COND_SYNTHESIZED")
            for i,j,k in pre_conditions:
                print(i, ",", j, ",", k)
                logger.debug(f"{i} {j} {k}")


