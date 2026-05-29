# Contents
1. [Introduction to the Tool](#introduction-to-the-tool)
1. [Installation with Docker](#installation-with-Docker)
1. [Installation without Docker](#installation-without-Docker)
1. [Running the tool](#running-the-tool)
1. [Benchmarks](#benchmarks)
1. [File Format](#File-Format)
1. [Reproducibility](#reproducibility-of-results)
1. [Citation](#Cite)
---
# Introduction to the Tool

This artifact is a prototype implementation of Real Program Synthesis. This tool takes as an input a set of polynomial constraints in SMT format, and input and output variables. The tool then outputs a program, that takes as input the rational values of input variables and gives as output the rational value of output variables.

---
# Installation with Docker
Docker submission required for CAV? TODO?

---
# Installation without Docker
## Requirements for installing the Tool
* sage (version >= 10.3)
* z3-solver (version >= 4.13)
* sympy (version >= 1.13.1)
* cvc5 (version >= 1.1.2)
* Some additional packages are required install using requirements.txt
<!-- * TODO: Some plog etc constraints from the existing -->

> **_NOTE:_**  Our tool works with the above requirements, but it may also work with older versions as well.

## Installing Tool

To install the tool do the following steps:
- Install [CVC5](https://cvc5.github.io/). Binary installation is available [here](https://github.com/cvc5/cvc5/releases).
To check the installation of cvc5 make sure that the command `cvc5 --sygus-qe-preproc --lang=sygus2 simple_sygus.sy` outputs the following:
```
(
(define-fun a_o ((delta_i Real)) Real 0.0)
)
```

- Install [SageMath](https://doc.sagemath.org/html/en/installation/index.html). 

The following commands may be useful to install SageMath:
    
    conda config --add channels conda-forge
    conda config --set channel_priority strict
    conda create -n sage sage python=3.9
    conda activate sage
    

To check that installation of sagemath make sure that the command `sage simple_qepcad_sage.sage` outputs the following:
```
delta >= 0 /\ 5000000 pi - 15707963 > 0 /\ 10000000 pi - 31415927 < 0 /\ skoS2 >= 0 /\ skoS2^2 - delta - 2 <= 0 /\ skoS2^2 + delta - 2 >= 0 /\ skoX > 0 /\ skoX - 1 < 0 /\ 1048576 skoX + 1048576 delta - 785407 >= 0 /\ 1048576 skoX - 1048576 delta - 785407 <= 0
```

- Execute the following command to install the python packages: `pip install -r requirements.txt` or `conda install --yes --file requirements.txt`

---
# Running the tool


## Phase 1
To run the Phase 1 of our tool run the following command on the SMT file containing constraints with path `file_path` and input-output variables in the file with path `ip_op_path`:
        
        python NQS/main_tool_cav.py file_path --ip_op_vars ip_op_path

For example `python NQS/main_tool_cav.py examples/NRA/smt_files/chosen_smt_files_asin_8_vars4_asin-8-vars4-chunk-0017.smt2 --ip_op_vars examples/NRA/ip_op_files/chosen_smt_files_asin_8_vars4_asin-8-vars4-chunk-0017.txt`.
Running this should create a file `program.py` which is the syntheized program.

## Phase 2
To run the Phase 2 of our tool run the following command on the SMT file containing constraints with path `file_path`, input-output variables in the file with path `ip_op_path`, and the file with path `path_pre_condition.smt` to save the pre-condition:

        python QEPCAD_SyGuS/main_tool_cav.py file_path path_pre_condition.smt --ip_op_vars ip_op_path

For example `python QEPCAD_SyGuS/qepcad_sygus.py examples/NRA/smt_files/chosen_smt_files_asin_8_vars4_asin-8-vars4-chunk-0011.smt2  pre_condition.smt --ip_op_vars examples/NRA/ip_op_files/chosen_smt_files_asin_8_vars4_asin-8-vars4-chunk-0011.txt`.
Running this should create a file `gus_program.py` which is the syntheized program.

## David Monniaux
To run the David Monniaux's approach run the following command on the SMT file containing constraints with path `file_path`, input-output variables in the file with path `ip_op_path`:

        python david_monniaux/dm_tool_cav.py file_path --ip_op_vars ip_op_path

For example `python david_monniaux/dm_tool_cav.py examples/NRA/smt_files/chosen_smt_files_asin_8_vars4_asin-8-vars4-chunk-0011.smt2 --ip_op_vars examples/NRA/ip_op_files/chosen_smt_files_asin_8_vars4_asin-8-vars4-chunk-0011.txt`.
Running this should create a file `dm_program.py` which is the syntheized program.

---
# Benchmarks
- NRA benchmarks are contained in the folder [examples/NRA](examples/NRA). The SMT files are in the directory [examples/NRA/smt_files](examples/NRA/smt_files/) and their corresponding input-output files are in the directory [examples/NRA/ip_op_files](examples/NRA/ip_op_files/)
- Synthethic benchmarks are contained in the folder [examples/synthethic_benchmarks](examples/synthetic_benchmarks). The SMT files are in the directory [examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir](examples/synthetic_benchmarks/synthetic_benchmarks_smt_dir/) and their corresponding input-output files are in the directory [examples/synthetic_benchmarks/synthetic_benchmarks_ip_op_dir/](examples/synthetic_benchmarks/synthetic_benchmarks_ip_op_dir/)
- Comfusy benchmarks are contained in the folder [examples/comfusy_benchmarks](examples/comfusy_benchmarks). The SMT files are in the directory [examples/comfusy_benchmarks/smt_files](examples/comfusy_benchmarks/smt_files/) and their corresponding input-output files are in the directory [examples/comfusy_benchmarks/ip_op_files](examples/comfusy_benchmarks/ip_op_files/)


One can take a look into [examples](examples/) folder for all the examples.

---
# File Format

## Input-Output File Format
In the input-output file the first line has a list of all the input variables separated by space:

`input_var1 input_var2 ...`

Then the next line lists the output variables:

`output_var1 output_var2 ...`

## Post-Condition SMT File

Standard [SMT](https://smt-lib.org/) file format.

---
# Reproducibility of results:

Execute the following commands to reproduce the results:

- For the NRA benchmarks execute the following:
`python ./script_execute_all_benchmarks.py examples/NRA/smt_files/ --ip_op_benchmark_dir examples/NRA/ip_op_files/`

- For the Comfusy benchmarks execute the following:
`python ./script_execute_all_benchmarks.py examples/comfusy_benchmarks/smt_files/ --ip_op_benchmark_dir examples/comfusy_benchmarks/ip_op_files/`

- For the Synthethic benchmarks execute the following:
`python ./script_execute_all_benchmarks.py examples/synthethic_benchmarks/synthethic_benchmarks_smt_files/ --ip_op_benchmark_dir examples/synthethic_benchmarks/synthethic_benchmarks_ip_op_dir/`

Executing each individually should produce the following files:
- our_method_logging_dir: This file contains the log files for all the Phase 1 execution of the benchmarks
- qepcad_logging_dir: This file contains the log files for all the Phase 2 execution of the benchmarks
- monniaux_logging_dir: This file contains the log files for all the David-Monniaux's execution of the benchmarks
- table_log.txt: This file contains the table of results

--
# Cite
```@misc{akshay2026programsynthesisnonlinearreal,
      title={Program Synthesis for Non-Linear Real Arithmetic: Going Beyond Realizability}, 
      author={S. Akshay and Supratik Chakraborty and R. Govind and Aniruddha R. Joshi},
      year={2026},
      eprint={2605.24263},
      archivePrefix={arXiv},
      primaryClass={cs.PL},
      url={https://arxiv.org/abs/2605.24263}, 
}```
