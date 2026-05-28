import sys
import os
import subprocess
import argparse
import parse_timer_log
import re
import random
# python script_execute_all_benchmarks.py ../chosen_smt_files_processed/


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



parser = argparse.ArgumentParser(description='script_execute', usage='%(prog)s [-h] [options] benchmark_dir', formatter_class=argparse.ArgumentDefaultsHelpFormatter)


##  arguments
parser.add_argument('benchmark_dir', help='path to post_condition SMT file', metavar='benchmark_dir')

parser.add_argument('--ip_op_benchmark_dir', help='path to input and output SMT files', metavar='benchmark_dir', default=None)

#phase 1
parser.add_argument('--our_method_logging_dir_mathematica', help='path of logging directory for our method', metavar='our_method_logging_dir_mathematica', default="our_method_logging_dir_mathematica", type=str)

parser.add_argument('--our_method_programs_dir_mathematica', help='path of logging directory for our method', metavar='our_method_programs_dir_mathematica', default="our_method_programs_dir_mathematica", type=str)

#path of generating the table
parser.add_argument('--table_log', help='path of generating the table', metavar='table_log', default="table_log.txt", type=str)

parser.add_argument('--timeout', help='timeout', metavar='timeout', default=120, type=int)



args = parser.parse_args()


benchmark_dir = args.benchmark_dir
our_method_logging_dir = args.our_method_logging_dir_mathematica
our_method_programs_dir = args.our_method_programs_dir_mathematica

timeout = args.timeout
table_log = args.table_log
ip_op_benchmark_dir = args.ip_op_benchmark_dir

random.seed(10)
with open(table_log, "w+") as f:
    f.write("")
# timeout = 120

# our_method_logging_dir = "our_method_logging_dir"
# our_method_programs_dir = "our_method_programs_dir"
# our_method_sygus_dir = "our_method_sygus_dir"
# our_method_sage_gen = "our_method_sage_gen"

# monniaux_logging_dir = "monniaux_logging_dir"
# monniaux_programs_dir = "monniaux_programs_dir"
# monniaux_sage_gen = "monniaux_sage_gen"

# qepcad_logging_dir = "qepcad_logging_dir"
# qepcad_sage_gen = "qepcad_sage_gen"

all_dirs = [our_method_logging_dir]

for dir in all_dirs:
    try:
        os.system(f"mkdir -p {dir}")
    except Exception as e:
        print(e)

    try:
        os.system(f"rm -rf {dir}/*")
    except Exception as e:
        print(e)




our_method_program = "python NQS_mathematica/main_tool.py"


all_files = []
for root, dirs, files in os.walk(benchmark_dir):
    # print(root, dirs, files)
    for file in files:
        file_path = os.path.join(root, file)
        if "smt" in file_path.split("/")[-1]:
            all_files.append(file_path)

all_files.sort()
print(all_files)

done_files = []
try:
    #done_files = ['examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_circles_fixed_radii.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_circles_higher_powers_fixed_centers.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_circles_higher_powers_fixed_centers2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_circles_origin_centre.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_complex_shapes.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_complex_shapes2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_complex_shapes3.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_2_power_4circles_origin_centre.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_3_dimensional_hyper_bola.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_circle_origin_centre.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_circle_origin_other_circle_radius_fixed.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_geometric3.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_geometric4.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_geometric5.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_geometric6.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_1_supratik_email_example.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_0.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_1.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_10.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_11.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_12.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_13.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_16.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_4.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_25_9.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_2_2_annular_circles_5_499.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_2_circles_origin_centre.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_2_power_4circles_origin_centre.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_3_circles.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_3_circles_modified.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_3_ellipses.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_hyper_bola.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_3_intersecting_hyperbolas.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input1.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input10.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input11.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input11_2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input12.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input12_2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input13.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input13_2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input14.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input14_2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input15.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input16.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input17.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input18.smt'] + [
    # 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input19.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input2.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input2_slack.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input3.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input4.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input5.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input7.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input8.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_input9.smt', 'examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/_all_synthetic_benchmarks_collated_4_kissing_set.smt']
    pass
except:
    pass

# exit(-1)

from datetime import datetime

log_file_information = []


# for i in all_files:
#     print(i)

# exit(-1)

heading = ["file_name", f"Our_tool_mathematica [timeout {timeout}s]", "z3_time", "mathematica_time","sygus_time", "irrational_points", "rational_points", "z3_calls", "mathematica_calls", "weakest_pre", "substitution_and_simplify_time", "program_writing_syn_time", "synthesized_program_time_total [=avg time*10 in sec]", "Z3_time_total [=avg time*10 in sec]", "synthesized_program_SAT", "synthesized_program_UNSAT", "synthesized_program_UNKNOWN", "z3_program_SAT", "synthesized_program_UNSAT", "synthesized_program_UNKNOWN", "Z3_irrational_point", " "]

log_file_information.append(heading)


for i in all_files:
    if i in done_files:
        continue
    # sygus_approach_status = ""
    # sygus_time = None

    our_approach_status = ""
    our_approach_time = None

    print()
    print(f"_____{i}__________________________________________")
    print()

    # random_seed = int(datetime.now().timestamp())
    # random_seed = 10
    file_name = "".join(i.replace("/","_").split(".")[:-1])



    command = f"rm -rf sage_files ip_op_vars.txt log.txt timer_log.txt program.py"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()
    
    
    ip_file_name = i

    if ip_op_benchmark_dir == None:
        if "zankl" in ip_file_name:
            want_ip_vars = ["b", "delta"]
            want_op_vars = ["a"]
        if "asin_8_vars4" in ip_file_name:
            want_ip_vars = ["delta", "skoX", "skoS2"]
            want_op_vars = ["skoSP", "skoSM"]
        if "asin_8_asin-8" in ip_file_name:
            want_ip_vars = ["delta", "skoX", "skoS2", "pi"]
            want_op_vars = ["skoSP","skoSM"]
        if "Arthan_M2" in ip_file_name:
            want_ip_vars = ["delta", "skoSINS", "skoM"]
            want_op_vars = ["skoCOSS", "skoS"]
        if "Arthan_KM2" in ip_file_name:
            want_ip_vars = ["delta", "skoS"]
            want_op_vars = ["skoCOSS","skoSINS"]
        if "Arthan_1C" in ip_file_name\
            or "Arthan_1A" in ip_file_name:
            want_ip_vars = ["delta", "skoS","pi"]
            want_op_vars = ["skoCOSS","skoSINS"]
        
        with open("ip_op_vars.txt","w") as f:
            print(" ".join(want_ip_vars), file=f)
            print(" ".join(want_op_vars), file=f)
        assert want_ip_vars!=[] and want_op_vars!=[], "ERROR want ip/op vars == []"
        assert False
    else:
        # for m in all_files:
        f_name = i.split("/")[-1].split(".")[0]
        if ip_op_benchmark_dir != None:
            print(i, ip_op_benchmark_dir+"/"+f_name+".txt")

        command = f"cp {ip_op_benchmark_dir}/{f_name}.txt ip_op_vars.txt"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(f"command: {command}")
        print(f"output: {result.stdout}, {result.stderr}")
        print()
    # continue
    
    ip_vars, op_vars = fetch_input_output_variables("ip_op_vars.txt")


    #TODO create an ip_op file and add things appropriately
    ####OUR APPROACH
    # command = f"timeout -s 15 -v {timeout}s {our_method_program} {i} --ip_op_vars ip_op_vars.txt"

    command = f"timeout -k 3s {timeout}s {our_method_program} {i} --ip_op_vars ip_op_vars.txt"

    time_then = datetime.now().timestamp()
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    time_now = datetime.now().timestamp()
    
    our_approach_time = time_now - time_then

    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}, {result.returncode}")
    print()
    
    if "sending signal TERM to command" in result.stderr or "Killed" in result.stderr or result.returncode in (124, 137, 9, -9):
        our_approach_status = "TIMEOUT"

        # print(f"AAAA: {our_approach_status}, {result.stderr}")
        # exit(-1)
    
        command = "pkill -9 -f WolframKernel"
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(f"command: {command}")
        print(f"output: {result.stdout}, {result.stderr}")
        print()

    # command = "cat log_file.log | grep \"First point\""
    # result = subprocess.run(command, shell=True, text=True, capture_output=True)
    # print(f"command: {command}")
    # print(f"output: {result.stdout}, {result.stderr}")
    # print()
    # assert result.stdout=="" or\
    #     "sat" == result.stdout.split(":")[-1].strip(),\
    #     f"first point unsat?! {result}"   

    command = f"tail -1 timer_log.txt"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()
    if "WEAKEST_PRE_COND_SYNTHESIZED" in result.stdout:
        assert our_approach_status!="TIMEOUT",\
                "Our approach timedout but we also found weakest pre-condition, how is this possible?"
        our_approach_status = "WEAKEST_PRE_CONDITION"
    
    command = f"mkdir -p {our_method_logging_dir}/{file_name}/"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()
    assert result.stderr == "", f"{result}"

    command = f"mv log.txt {our_method_logging_dir}/{file_name}/"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()
    assert result.stderr == "", f"{result}"

    z3_time, cad_time, sygus_time, irrational_points, rational_points, z3_calls, sage_calls, weakest_pre, program_synthesized,subs_simplify_time, prog_syn_time = parse_timer_log.parse_timer_file(file_name="timer_log.txt",timeout=timeout)

    log_file_information.append([i, "Our_tool", z3_time, cad_time,sygus_time, irrational_points, rational_points, z3_calls, sage_calls, weakest_pre, subs_simplify_time, prog_syn_time ])

    #evaluate the synthesized program from our side for 10 uniformly randomly selected inputs
    sat_count = 0
    unsat_count = 0
    unknown_count = 0

    sat_count_z3 = 0
    unsat_count_z3 = 0
    unknown_count_z3 = 0

    total_prog_time = 0
    total_z3_prog_time = 0

    z3_irrational = 0

    #Comment out so that program execution does not happen for partially written programs. Sometimes it may happen by accident that the timeout is triggered with the main code is writing the program. This happens often for a particular benchmark _all_synthetic_benchmarks_collated_1_geometric3, so when this happens the partially written program is executed in the following commented blocks -- causing an error.
    """ 
    for _ in range(10):
        with open("values_file.txt","w") as f:
            for ip_var in ip_vars:
                sign = random.choice([-1,1])
                number = random.random()
                if number == 0:
                    number = 0.1
                ip_num = int(number*1000)
                ip_denm = 1000
                print(ip_num, file = f, flush = True)
                print(ip_denm, file = f, flush = True)
                print(ip_num)
                print(ip_denm)
        
        
        command = f"timeout -s 15 -v {timeout} python program.py < values_file.txt"
        
        time_then = datetime.now().timestamp()
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        time_now = datetime.now().timestamp()
        total_prog_time += (time_now-time_then)
        print(f"command: {command}")
        print(f"output: {result.stdout}, {result.stderr}")
        print()
        if "No such file or directory" in result.stderr or "sending signal TERM to command" in result.stderr:
            unknown_count += 1
            total_prog_time = -1
        else:
            if "UNSAT" in result.stdout:
                unsat_count += 1
            elif "UNKNOWN" in result.stdout:
                unknown_count += 1
            else:
                assert "SAT" in result.stdout, f"{result.stdout}"
                sat_count += 1
            assert result.stderr == "", f"{result}"




        command = f"timeout -s 15 -v {timeout} python z3_program.py {i} ip_op_vars.txt< values_file.txt"
        
        time_then = datetime.now().timestamp()
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        time_now = datetime.now().timestamp()
        total_z3_prog_time += (time_now-time_then)
        print(f"command: {command}")
        print(f"output: {result.stdout}, {result.stderr}")
        print()
        # if "SIGTERM" in result.stderr:
        #     unknown_count_z3 += 1
        
        if "UNSAT" in result.stdout:
            unsat_count_z3 += 1
        elif "UNKNOWN" in result.stdout or "sending signal TERM to command" in result.stderr:
            unknown_count_z3 += 1
        else:
            assert "SAT" in result.stdout
            sat_count_z3 += 1
        assert result.stderr == "" or "sending signal TERM to command" in result.stderr, f"{result}"

        z3_irrational += ("IRRATIONAL" in result.stdout)
        print(unknown_count, unsat_count, sat_count)
        print(unknown_count_z3, unsat_count_z3, sat_count_z3)


        # "synthesized_program_time_total [=avg time*10 in sec]", "Z3_time_total [=avg time*10 in sec]", "synthesized_program_SAT", "synthesized_program_UNSAT", "synthesized_program_UNKNOWN", "z3_program_SAT", "synthesized_program_UNSAT", "synthesized_program_UNKNOWN", " "
    
    """    
    
    
    log_file_information[-1]+=[total_prog_time, total_z3_prog_time, sat_count, unsat_count, unknown_count, sat_count_z3, unsat_count_z3, unknown_count_z3,z3_irrational ," "]



    # exit(-1)

    command = f"mv timer_log.txt {our_method_logging_dir}/{file_name}/"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()
    assert result.stderr == "", f"{result}"


    command = f"mv program.py {our_method_logging_dir}/{file_name}/"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()



    command = f"cp ip_op_vars.txt {our_method_logging_dir}/{file_name}/"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()

    print("STATUS:", our_approach_status)
    print("TIME:", our_approach_time)
    # continue

    command = f"rm pre_condition.smt2"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(f"command: {command}")
    print(f"output: {result.stdout}, {result.stderr}")
    print()


    # print
    # continue
    with open(table_log,"w+") as f:
        for i in log_file_information:
            print(",".join([str(j) for j in i]), file=f, flush=True)
    
    # continue
    print()
    print()













    

print()
print()
print()
with open(table_log,"w+") as f:
    for i in log_file_information:
        print(",".join([str(j) for j in i]), file=f, flush=True)
    # continue













# if our_approach_status == "":
#     os.system(f"cp log_file.log {our_method_logging_dir}/{file_name}_log.log")
    
#     # os.system(f"cat log_file.log | grep \"First point\" ")
#     first_point_sat = "cat log_file.log | grep \"First point\""
#     result = subprocess.run(first_point_sat, shell=True, text=True, capture_output=True)
#     if "unsat" in str(first_point_sat.stdout):
#         our_approach_status = "first_point_unsat"
#     else:
#         os.system(f"cp program.py {our_method_programs_dir}/{file_name}.py")
#         os.system(f"{synthesize_sygus_command} {i} {our_method_sygus_dir}/{file_name}.sy")
# os.system(f"{sygus_command} {our_method_sygus_dir}/{file_name}.sy > {our_method_sygus_dir}/{file_name}_result.txt")

# os.system(f"timeout -60s {monniaux_program} {i} {random_seed}")
# os.system(f"cp program.py {monniaux_programs_dir}/{file_name}.py")
# os.system(f"cp log_file.log {monniaux_logging_dir}/{file_name}_log.log")



