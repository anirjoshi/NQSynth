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
import timeit
import argparse
import ast
import signal
import sys
import os  # <-- Make sure 'os' is imported

sys.path.append("lib")

# Import wolframclient for Mathematica bindings
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
import atexit

#convert the second input into smt format
import convert_input_smt_format

#the following converts from z3 sexpr to sympy and returns it
from smt_sympy_converter import sexpr_to_sympy

#the following converts from sympy to z3
from sympy_z3 import sympy_to_z3


class SympySyntaxTransformer(ast.NodeTransformer):
    """
    Safely intercepts Python comparisons (A == B) and rewrites them as Eq(A, B).
    Also intercepts Python logicals (and, or, not) and rewrites them as 
    SymPy logical functions (And, Or, Not) to avoid Relational truth TypeErrors.
    """
    def visit_Compare(self, node):
        self.generic_visit(node)
        # Only transform single '==' comparisons
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
            return ast.Call(
                func=ast.Name(id='Eq', ctx=ast.Load()),
                args=[node.left, node.comparators[0]],
                keywords=[]
            )
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        # Convert `and` / `or` to SymPy's `And` / `Or`
        func_name = 'And' if isinstance(node.op, ast.And) else 'Or'
        return ast.Call(
            func=ast.Name(id=func_name, ctx=ast.Load()),
            args=node.values,
            keywords=[]
        )

    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        # Convert `not` to SymPy's `Not`
        if isinstance(node.op, ast.Not):
            return ast.Call(
                func=ast.Name(id='Not', ctx=ast.Load()),
                args=[node.operand],
                keywords=[]
            )
        return node

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
    assert ("/" in point) or (int(point)==float(point)),\
        "ERROR point returned by z3 is not rational"

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


def sample_rational():
    # Random numerator and denominator
    numerator = random.randint(0, 1000)  # Random numerator
    denominator = random.randint(1, 1000)  # Random denominator, non-zero
    
    # Ensure it's between 0 and 1
    if numerator > denominator:
        numerator, denominator = denominator, numerator
    
    return (numerator, denominator)


def synthesize_program(file_name, pre_conditions, post_condition, ip_vars, op_vars, lambda_var, weakest_pre_condition=False):
    tmp = sys.stdout
    sys.stdout = open(file_name, "w+")

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
        
        print()
        print(f"\teval = pre_cond.subs(",'{',", ".join(["\'"+var+"\':"+var for var in ip_vars]),'})')

        print()
        print(f"\tif eval==True:")
        print(f"\t\tassert eval!=False")
        print(f"\t\treturn True")
        print(f"\treturn False")
        print()
    
    #write a post-condition evaluation function
    all_vars = ", ".join([f"{i}:sympy.Rational" for i in ip_vars+op_vars])
    
    print()
    print(f"def post_condition({all_vars}):")    

    print("\t#",str(post_condition))
    print()
    print("\tpost_cond = ",sympy.srepr(post_condition))
    print()
    print(f"\teval = post_cond.subs(",'{',", ".join(["\'"+var+"\':"+var for var in ip_vars+op_vars]),'})')

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
    print(f"\teval = post_cond.subs(",'{',", ".join(["\'"+var+"\':"+var for var in ip_vars+op_vars]),'})')
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
        print("\t\t\tprint(\"SAT\")")
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


if __name__=="__main__":


    kernel_path = '/Applications/Wolfram Engine.app/Contents/MacOS/WolframKernel'
    print(f"Starting Wolfram Session at {kernel_path}...")
    session = WolframLanguageSession(kernel_path)
    
    # Define the optimized signal handler
    def handle_sigterm(signum, frame):
        print("\n[TIMEOUT] Forcefully terminating background Wolfram Engine...")
        try:
            session.terminate()  # Tell the kernel process to die
        except:
            pass
        os._exit(1)  # <-- USE THIS: Hard exit to prevent Python from hanging!

    # Intercept the 'timeout' command's kill signal
    signal.signal(signal.SIGTERM, handle_sigterm)
    
    session.start()
    
    import atexit
    atexit.register(lambda: session.terminate())

    # kernel_path = '/Applications/Wolfram Engine.app/Contents/MacOS/WolframKernel'
    # print(f"Starting Wolfram Session at {kernel_path}...")
    # session = WolframLanguageSession(kernel_path)
    # session.start()
    
    # --- THE EASIEST FIX ---
    # Instantly throw a built-in error to break the network block.
    # We don't catch it. We just let it crash the script.
    # def handle_sigterm(signum, frame):
    #     raise TimeoutError("\n[TIMEOUT] The bash timeout command killed the script!")
        
    # signal.signal(signal.SIGTERM, handle_sigterm)
    # -----------------------

    
    # Because it crashes with a standard error, Python will automatically 
    # run this atexit hook for you before dying, cleaning up the zombies!
    # import atexit
    # atexit.register(lambda: session.terminate())


    # # ==========================================
    # # START PERSISTENT MATHEMATICA SESSION
    # # ==========================================
    # kernel_path = '/Applications/Wolfram Engine.app/Contents/MacOS/WolframKernel'
    # print(f"Starting Wolfram Session at {kernel_path}...")
    # session = WolframLanguageSession(kernel_path)

    # # 2. Forced cleanup for when the 'timeout' command sends a SIGTERM
    # # 2. Define the cleanup handler function BEFORE session.start()
    # def handle_sigterm(signum, frame):
    #     print("\n[TIMEOUT] Cleanly terminating background Wolfram Engine...")
    #     try:
    #         session.terminate()
    #     except:
    #         pass
    #     sys.exit(1)
    # # # Define the optimized signal handler
    # # def handle_sigterm(signum, frame):
    # #     print("\n[TIMEOUT] Forcefully terminating background Wolfram Engine...")
    # #     try:
    # #         session.terminate()  # Tell the kernel process to die
    # #     except:
    # #         pass
    # #     os._exit(1)  # <-- USE THIS: Hard exit to prevent Python from hanging!
        
    # # Bind the SIGTERM signal to our cleanup function
    # signal.signal(signal.SIGTERM, handle_sigterm)


    # session.start()
    
    # # Ensure the background engine is properly killed on termination
    # atexit.register(lambda: session.terminate())

    parser = argparse.ArgumentParser(description='NQS', usage='%(prog)s [-h] [options] post_condition', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ##  arguments
    parser.add_argument('post_condition', help='path to post_condition SMT file', metavar='post_condition')
    parser.add_argument('--ip_op_vars', help='path to input output variables file',type=str, default="ip_op_vars.txt")
    parser.add_argument('--random_seed', help='random seed', type=int, default=10)
    parser.add_argument('--sage_command', help='[DEPRECATED] command to run a sage file', type=str, default="sage")
    parser.add_argument('--log_file', help='path to log file', type=str, default="log.txt")
    parser.add_argument('--timer_log_file', help='path to timer log file', type=str, default="timer_log.txt")
    parser.add_argument('--sage_dir', help='[DEPRECATED] directory name for sage files', type=str, default="sage_files")
    parser.add_argument('--program_name', help='name of the program file', type=str, default="program.py")

    args = parser.parse_args()
    
    post_condition_file = args.post_condition
    ip_op_vars_file = args.ip_op_vars
    random_seed = args.random_seed
    log_file_name = args.log_file
    timer_logs_file = args.timer_log_file
    op_program_file_name = args.program_name

    iteration_index = 0
    lambda_var_prefix = "lambda_var"
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
        ip_vars = []
        op_vars = []

        assert len(sys.argv) > 2, "need a file with input and output variables"
        ip_vars, op_vars = fetch_input_output_variables(input_output_variables_file_path=input_output_variables_file_name)
      
    
    assert len(ip_vars + op_vars) == len(set(ip_vars+op_vars)), f"Repeating variables {ip_vars + op_vars}"

    logger.debug(f"ip_vars: {ip_vars}")
    logger.debug(f"op_vars: {op_vars}")

    # create a new_lambda rational variable
    tmp_lambda_index = 0
    lambda_var = lambda_var_prefix + "_" + str(tmp_lambda_index)
    while lambda_var in ip_vars + op_vars:
        tmp_lambda_index += 1
        lambda_var = lambda_var_prefix + "_" + str(tmp_lambda_index)
    
    logger.debug(f"lambda_var: {lambda_var}")

    sympy_lambda_var = sympy.symbols(lambda_var)

    assert lambda_var not in ip_vars+op_vars, f"lambda_var={lambda_var} in {ip_vars+op_vars}"

    #read the post condition from the SMT file directly
    post_condition = z3.And(z3.parse_smt2_file(ip_file_name))
    sexpr_str = post_condition.sexpr()
    
    logger.debug(f"post_condition_smt:{post_condition}")

    # Convert post_condition to SymPy
    symbols_set, sympy_expr = sexpr_to_sympy(sexpr_str)

    for free_vars in sympy_expr.free_symbols:
        assert str(free_vars) in ip_vars + op_vars, f"Error {str(free_vars)} not in the list of input and output variables"
    
    #remove the output variables not present in the formula
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

    directions = [[sympy.Rational(0,1) if j!=i else sympy.Rational(1,1) for j in range(len(op_vars))] for i in range(len(op_vars))]

    logger.debug(f"DIRECTIONS: {len(directions)}:{directions}")
    
    print("working...")

    symbols_sympy_dict = {str(i):i for i in sympy_expr.free_symbols}
    
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
        # Add this before exiting early
        session.terminate()
        exit(-1)
    
    pre_conditions = []

    while is_solution == z3.sat:
        logger.debug("")
        logger.debug(f"---------point-synthesis-------------")
        
        m = s.model()
        
        is_solution_rational = True
        model_vals = []

        for str_var, z3_var in vars_dict.items():
            try:
                convert_rational = convert_string_rational(str(m[z3_var]))
            except:
                logger.debug("IRRATIONAL")
                logger.debug("model:"+", ".join([str(i)+"="+str(m[j]) for i,j in vars_dict.items()]))
                print("IRRATIONAL")
                
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

        sympy_vals = {i[0]: sympy.Rational(i[1][0],i[1][1]) for i in model_vals}

        for direction in directions:
            substitution = dict()
            for i in range(len(op_vars)):
                op_var = op_vars[i]
                if op_var not in symbols_sympy_dict.keys():
                    new_symbol = sympy.symbols(op_var)
                    substitution[new_symbol] = sympy.Rational(0,1) + sympy_lambda_var*direction[i]    
                else:
                    substitution[symbols_sympy_dict[op_var]] = sympy_vals[op_var] + sympy_lambda_var*direction[i]
            
            logger.debug(f"---------pre-condition {iteration_index}---------")
            logger.debug(f"direction: {direction}")
            logger.debug(f"substitution: {substitution}")
            print()
            print("direction:",direction)
            print("substitution:", substitution)

            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_SUBS_SIMPLIFY_START:", current_time, file=f, flush=True)

            sub_expr = sympy_expr.subs(substitution)
            sub_expr = sub_expr.simplify()

            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_SUBS_SIMPLIFY_STOP:", current_time, file=f, flush=True)
            
            print(sub_expr)
    
            if str(lambda_var) in [str(m) for m in sub_expr.free_symbols]:
                # ==========================================
                # NATIVE MATHEMATICA QUANTIFIER ELIMINATION
                # ==========================================

                # 1. Helper to recursively convert SymPy AST to Mathematica Logical Syntax
                def sympy_to_mathematica_logic(expr):
                    from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
                    from sympy.core.relational import Eq, Ne, GreaterThan, LessThan, StrictGreaterThan, StrictLessThan
                    
                    if isinstance(expr, And):
                        return "(" + " && ".join(sympy_to_mathematica_logic(arg) for arg in expr.args) + ")"
                    elif isinstance(expr, Or):
                        return "(" + " || ".join(sympy_to_mathematica_logic(arg) for arg in expr.args) + ")"
                    elif isinstance(expr, Not):
                        return "!(" + sympy_to_mathematica_logic(expr.args[0]) + ")"
                    elif isinstance(expr, Implies):
                        return "Implies[" + sympy_to_mathematica_logic(expr.args[0]) + ", " + sympy_to_mathematica_logic(expr.args[1]) + "]"
                    elif isinstance(expr, Equivalent):
                        return "Equivalent[" + sympy_to_mathematica_logic(expr.args[0]) + ", " + sympy_to_mathematica_logic(expr.args[1]) + "]"
                    elif isinstance(expr, Eq):
                        return sympy_to_mathematica_logic(expr.lhs) + " == " + sympy_to_mathematica_logic(expr.rhs)
                    elif isinstance(expr, Ne):
                        return sympy_to_mathematica_logic(expr.lhs) + " != " + sympy_to_mathematica_logic(expr.rhs)
                    elif isinstance(expr, GreaterThan):
                        return sympy_to_mathematica_logic(expr.lhs) + " >= " + sympy_to_mathematica_logic(expr.rhs)
                    elif isinstance(expr, LessThan):
                        return sympy_to_mathematica_logic(expr.lhs) + " <= " + sympy_to_mathematica_logic(expr.rhs)
                    elif isinstance(expr, StrictGreaterThan):
                        return sympy_to_mathematica_logic(expr.lhs) + " > " + sympy_to_mathematica_logic(expr.rhs)
                    elif isinstance(expr, StrictLessThan):
                        return sympy_to_mathematica_logic(expr.lhs) + " < " + sympy_to_mathematica_logic(expr.rhs)
                    else:
                        # Base condition: Replace python power ** with mathematica ^
                        return str(expr).replace("**", "^")

                # 2. Format SymPy expression into Mathematica Syntax
                math_expr = sympy_to_mathematica_logic(sub_expr)



                # 3. Construct the Quantifier Elimination Query String
                # Resolving it directly over the Reals as established
                # *ADDED LogicalExpand to break apart chained `Inequality` wrappers*
                query_str = f"ToString[LogicalExpand[Resolve[Exists[{lambda_var}, {math_expr}], Reals]], InputForm]"
                query_str = query_str.replace("_","$")
                print("math_cmd:", query_str)
                
                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_MATHEMATICA_START:", current_time, file=f, flush=True)

                # Execute the string query against the active background engine
                math_result = session.evaluate(wlexpr(query_str))

                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_MATHEMATICA_FINISH:", current_time, file=f, flush=True)


                # 4. Clean up Mathematica's output string safely for SymPy parsing
                pre_cond_str = str(math_result)
                pre_cond_str = pre_cond_str.replace("$","_")
                # *NEW*: Convert Mathematica brackets to Python parentheses so it doesn't subscript
                pre_cond_str = pre_cond_str.replace("[", "(").replace("]", ")")
                # *NEW*: Map Mathematica's Sqrt to SymPy's sqrt
                pre_cond_str = pre_cond_str.replace("Sqrt", "sqrt")

                # Convert Mathematica logical operators to Python equivalents safely
                pre_cond_str = pre_cond_str.replace("&&", " and ").replace("||", " or ")
                
                # Safely replace "!" with " not " (without breaking "!=" operators)
                pre_cond_str = pre_cond_str.replace("!=", "NEQ_TEMP").replace("!", " not ").replace("NEQ_TEMP", "!=")
                
                # Convert power operators
                pre_cond_str = pre_cond_str.replace("^", "**")
                # Fix boolean types
                pre_cond_str = pre_cond_str.replace("True", "True").replace("False", "False")



                # ---------------------------------------------------------
                # 5. AST Transformation: Safely convert `A == B` into `Eq(A, B)`
                #    and Python logicals into SymPy `And`, `Or`, `Not`
                # ---------------------------------------------------------
                tree = ast.parse(pre_cond_str, mode='eval')
                tree = SympySyntaxTransformer().visit(tree)
                pre_cond_str = ast.unparse(tree)

                logger.debug(f"PRECOND_{iteration_index}: {pre_cond_str}")


                # 6. Convert String back to SymPy logic
                local_vars = {str(sym): sym for sym in sub_expr.free_symbols}
                sympy_pre_cond = sympy.sympify(pre_cond_str, locals=local_vars)
                logger.debug(f"PRECOND_SYMPY_{iteration_index}: {sympy_pre_cond}")

            else:
                current_time = timeit.default_timer()
                with open(timer_logs_file,"a") as f:
                    print("TIME_MATHEMATICA_START:", current_time, file=f, flush=True)
                    print("TIME_MATHEMATICA_FINISH:", current_time, file=f, flush=True)
                
                pre_cond = sub_expr
                logger.debug(f"PRECOND_{iteration_index}: {pre_cond}")
                sympy_pre_cond = sub_expr
                pre_cond = None
                sub_expr = None
            
            iteration_index+=1

            pre_conditions.append((sympy_pre_cond.copy(), sympy_vals.copy(), substitution.copy()))

            pre_cond_z3 = sympy_to_z3(sympy_pre_cond, vars_dict)
            
            s.add(z3.Not(pre_cond_z3))
            
            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_PROG_SYN_START:", current_time, file=f, flush=True)
            synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr, ip_vars=ip_vars, op_vars=op_vars, lambda_var=lambda_var)
            current_time = timeit.default_timer()
            with open(timer_logs_file,"a") as f:
                print("TIME_PROG_SYN_FINISH:", current_time, file=f, flush=True)

        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_Z3_START:", current_time, file=f, flush=True)
        is_solution = s.check()
        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_Z3_FINISH:", current_time, file=f, flush=True)

    print()
    if is_solution == z3.unsat:
        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_PROG_SYN_START:", current_time, file=f, flush=True)
        synthesize_program(file_name=op_program_file_name, pre_conditions=pre_conditions,post_condition=sympy_expr,ip_vars=ip_vars,op_vars=op_vars, lambda_var=lambda_var, weakest_pre_condition=True)
        current_time = timeit.default_timer()
        with open(timer_logs_file,"a") as f:
            print("TIME_PROG_SYN_STOP:", current_time, file=f, flush=True)

        print("WEAKEST_PRE_COND_SYNTHESIZED")
        with open(timer_logs_file, "a") as f:
            print("WEAKEST_PRE_COND_SYNTHESIZED", file=f, flush=True)
        logger.debug("WEAKEST_PRE_COND_SYNTHESIZED")
        for i,j,k in pre_conditions:
            print(i, ",", j, ",", k)
            logger.debug(f"{i} {j} {k}")
        
        # Add this right at the end of the script!
        session.terminate()