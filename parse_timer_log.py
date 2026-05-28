import os
import sys
import re


def parse_timer_file(file_name, timeout = 120):
    assert file_name!=None
    # print("TIMER_LOG", file_name)
    with open(file=file_name, mode="r") as f:
        all_lines = f.readlines()
        all_lines = [i.strip().strip("\n") for i in all_lines]
        all_lines = [re.sub(r'\s+', '', i) for i in all_lines if re.sub(r'\s+', '', i)!=""]

    z3_time = 0.0
    cad_time = 0.0
    sygus_time = 0.0
    subs_simplify_time = 0.0
    prog_syn_time = 0.0
    maple_time = 0.0
    mathematica_time = 0.0

    sage_calls = 0
    z3_calls = 0
    maple_calls = 0
    mathematica_calls = 0

    irrational_points = 0
    rational_points = 0

    weakest_pre = False
    
    current_status = None

    program_synthesized = None
    program_start_time = None

    for line in all_lines:
        print(line)

        if program_start_time==None and ":" in line.lower():
            program_start_time = float(line.split(":")[-1])

        if "z3" in line.lower():
            if "start" in line.lower():
                z3_start_time = float(line.split(":")[-1])
                current_status = "z3"
                z3_calls += 1
            if "stop" in line.lower() or "finish" in line.lower():
                z3_stop_time = float(line.split(":")[-1])
                z3_time += (z3_stop_time - z3_start_time)
                current_status = "point_type"
                z3_start_time = None
                z3_stop_time = None

        elif "rational" in line.lower()[:len("rational")]:
            rational_points += 1
            current_status = None
        
        elif "irrational" in line.lower()[:len("irrational")]:
            irrational_points += 1
            current_status = None
        
        elif "sage" in line.lower():
            if "start" in line.lower():
                sage_start_time = float(line.split(":")[-1])
                current_status = "sage"
                sage_calls += 1
            if "stop" in line.lower()  or "finish" in line.lower():
                sage_stop_time = float(line.split(":")[-1])
                cad_time += sage_stop_time - sage_start_time
                # print(cad_time,sage_stop_time,sage_start_time, sage_stop_time - sage_start_time )
                current_status = None
                sage_start_time = None
                sage_stop_time = None
        elif "maple" in line.lower():
            if "start" in line.lower():
                maple_start_time = float(line.split(":")[-1])
                current_status = "maple"
                maple_calls += 1
            if "stop" in line.lower()  or "finish" in line.lower():
                maple_stop_time = float(line.split(":")[-1])
                cad_time += maple_stop_time - maple_start_time
                # print(cad_time,sage_stop_time,sage_start_time, sage_stop_time - sage_start_time )
                current_status = None
                maple_start_time = None
                maple_stop_time = None
        elif "mathematica" in line.lower():
            if "start" in line.lower():
                mathematica_start_time = float(line.split(":")[-1])
                current_status = "mathematica"
                mathematica_calls += 1
            if "stop" in line.lower()  or "finish" in line.lower():
                mathematica_stop_time = float(line.split(":")[-1])
                cad_time += mathematica_stop_time - mathematica_start_time
                # print(cad_time,sage_stop_time,sage_start_time, sage_stop_time - sage_start_time )
                current_status = None
                mathematica_start_time = None
                mathematica_stop_time = None
        elif "sygus" in line.lower():
            if "start" in line.lower():
                sygus_start_time = float(line.split(":")[-1])
                current_status = "sygus"
            if "stop" in line.lower()  or "finish" in line.lower():
                sygus_stop_time = float(line.split(":")[-1])
                sygus_time += sygus_stop_time - sygus_start_time
                current_status = None
                sygus_stop_time = None
                sygus_start_time = None

        elif "TIME_SUBS_SIMPLIFY_START".lower() in line.lower():
            subs_simplify_start = float(line.split(":")[-1])
            current_status = "subs_simplify"
        elif "TIME_SUBS_SIMPLIFY_STOP".lower() in line.lower() or "TIME_SUBS_SIMPLIFY_FINISH".lower() in line.lower():
            subs_simplify_stop = float(line.split(":")[-1])
            subs_simplify_time += (subs_simplify_stop-subs_simplify_start)
            current_status = None
        
        elif "TIME_PROG_SYN_START".lower() in line.lower():
            prog_syn_time_start = float(line.split(":")[-1])
            current_status = "prog_syn"
        elif "TIME_PROG_SYN_STOP".lower() in line.lower() or "TIME_PROG_SYN_FINISH".lower() in line.lower():
            prog_syn_time_stop = float(line.split(":")[-1])
            prog_syn_time += (prog_syn_time_stop-prog_syn_time_start)
            current_status = None
                

        elif "weakest" in line.lower():
            weakest_pre = True
            current_status = None
        
        elif "ERROR_UNKNOWN_TERMINATION".lower() in line.lower():
            weakest_pre = False
            current_status = None
            
        
        elif "PROGRAM".lower() in line.lower() and "SYNTHESIZED".lower() in line.lower():
            program_synthesized = True
            current_status = None
    
        

    if current_status == "z3":
        z3_time += timeout - (z3_start_time - program_start_time)
        current_status = None
    elif current_status == "sage":
        cad_time += timeout - (sage_start_time - program_start_time)
        # print(cad_time)
        current_status = None
    elif current_status == "maple":
        cad_time += timeout - (maple_start_time - program_start_time)
        current_status = None
    elif current_status == "mathematica":
        cad_time += timeout - (mathematica_start_time - program_start_time)
        current_status = None
    elif current_status == "sygus":
        sygus_time += timeout - (sygus_start_time - program_start_time)
        current_status = None
    if current_status !=None:
        print("POSSIBLE_ERROR_CURRENT_STATUS NOT_NONE", current_status)
        print("RETURNING:", z3_time, cad_time, sygus_time, irrational_points, rational_points, z3_calls, sage_calls+maple_calls+mathematica_calls, weakest_pre, program_synthesized, subs_simplify_time, prog_syn_time)
        # print("RETURNING:", z3_time, cad_time, sygus_time, irrational_points, rational_points, z3_calls, maple_calls, weakest_pre, program_synthesized, subs_simplify_time, prog_syn_time)
    # assert current_status == None, f"{current_status}, {z3_time}, {cad_time}, {sygus_time}"
    # print(z3_time, cad_time, sygus_time, irrational_points, rational_points, z3_calls, sage_calls, weakest_pre)
    
    return z3_time, cad_time, sygus_time, irrational_points, rational_points, z3_calls, sage_calls+maple_calls+mathematica_calls, weakest_pre, program_synthesized, subs_simplify_time, prog_syn_time

if __name__=="__main__":
    assert len(sys.argv) > 1
    file_name = sys.argv[1]
    s = parse_timer_file(file_name=file_name)
    print(s)
    
