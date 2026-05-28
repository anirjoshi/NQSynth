import sys
import os
import subprocess
import argparse
import re
import random
# python script_execute_all_benchmarks.py ../chosen_smt_files_processed/

parser = argparse.ArgumentParser(description='script_execute', usage='%(prog)s [-h] [options] benchmark_dir', formatter_class=argparse.ArgumentDefaultsHelpFormatter)


##  arguments
parser.add_argument('benchmark_dir', help='path to post_condition SMT file', metavar='benchmark_dir')



args = parser.parse_args()


benchmark_dir = args.benchmark_dir

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





all_files = []
for root, dirs, files in os.walk(benchmark_dir):
    # print(root, dirs, files)
    for file in files:
        file_path = os.path.join(root, file)
        if "smt" in file_path.split("/")[-1]:
            all_files.append(file_path)

all_files.sort()
print(all_files)

# exit(-1)

from datetime import datetime

log_file_information = []


# for i in all_files:
#     print(i)

# exit(-1)




for i in all_files:


    print()
    print(f"_____{i}__________________________________________")
    print()

    # random_seed = int(datetime.now().timestamp())
    # random_seed = 10
    file_name = "".join(i.replace("/","_").split(".")[:-1])

    
    
    ip_file_name = i

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
    f_name = i.split("/")[-1].split(".")[0]
    print(f_name)
    print(" ".join(want_ip_vars))
    print(" ".join(want_op_vars))
    with open(f"{f_name}.txt","w") as f:
        print(" ".join(want_ip_vars), file=f)
        print(" ".join(want_op_vars), file=f)
    assert want_ip_vars!=[] and want_op_vars!=[], "ERROR want ip/op vars == []"

    continue
    