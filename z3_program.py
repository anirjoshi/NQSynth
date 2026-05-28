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


parser = argparse.ArgumentParser(description='NQS', usage='%(prog)s [-h] [options] post_condition ip_op_vars', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

##  arguments
parser.add_argument('post_condition', help='path to post_condition SMT file', metavar='post_condition')

parser.add_argument('ip_op_vars', help='path to input output variables file',type=str, default="ip_op_vars.txt")


args = parser.parse_args()

post_condition_file = args.post_condition
ip_op_vars_file = args.ip_op_vars

post_condition = z3.And(z3.parse_smt2_file(post_condition_file))

ip_vars, op_vars = fetch_input_output_variables(ip_op_vars_file)

z3_real_ips = [z3.Real(ip_var) for ip_var in ip_vars]
z3_vars = z3_real_ips + [z3.Real(op_var) for op_var in op_vars]
for ip_var, index in zip(ip_vars, range(len(ip_vars))):
    ip_0=int(input(f"enter numerator of {ip_var}:\n"))
    ip_1=int(input(f"enter denominator of {ip_var}:\n"))
    assert ip_1!=0, "Denominator entered is 0!"
    post_condition = z3.And(post_condition,z3_real_ips[index]==(ip_0/ip_1))

# print(post_condition)
S = Solver()
S.add(post_condition)
status = S.check()
if status == z3.sat:
    m = S.model()
    for z3_var in z3_vars:

        try:
            convert_rational = convert_string_rational(str(m[z3_var]))
            print(z3_var, convert_rational)
        except:

            print("IRRATIONAL")
            break

    print("SAT")
elif status == z3.unsat:
    print("UNSAT")
else:
    print("UNKNOWN")