# NQSynth: Program Synthesis for Non-Linear Real Arithmetic

NQSynth is a program synthesis tool for Non-Linear Real Arithmetic (NRA) specifications. Going beyond standard realizability, it handles unrealizable specifications by generating programs that yield outputs partially satisfying the constraints or explicitly reporting non-existence. Operating strictly on rational arithmetic, it synthesizes expressive, rounding-error-free code.

## Table of Contents
1. [Introduction to the Tool](#introduction-to-the-tool)
2. [Key Features](#key-features)
3. [How It Works](#how-it-works)
4. [Installation & Requirements](#installation--requirements)
   - [System Requirements](#system-requirements)
   - [Detailed Installation Steps](#detailed-installation-steps)
5. [File Formats](#file-formats)
6. [Running the Tool](#running-the-tool)
   - [Basic Usage](#basic-usage)
   - [Advanced Modes & Phases](#advanced-modes--phases)
   - [Available Options](#available-options)
7. [Benchmarks & Examples](#benchmarks--examples)
8. [Reproducibility of Results](#reproducibility-of-results)
9. [Citation](#citation)

---

## Introduction to the Tool
This artifact is a prototype implementation of Real Program Synthesis. Automated program synthesis from Non-Linear Real Arithmetic (NRA) specifications has wide-ranging applications. However, existing Syntax-Guided Synthesis (SyGuS) tools generally fail when presented with an "unrealizable" specification—one where valid outputs do not exist for certain inputs. 

NQSynth overcomes this limitation by synthesizing programs from *arbitrary* NRA specifications. This tool takes as an input a set of polynomial constraints in SMT format, and input and output variables. The tool then outputs a program that takes as input the rational values of input variables and gives as output the rational value of output variables. For any given input, the synthesized program will either:
1. Compute and output a valid rational result that satisfies the specification.
2. Accurately report the non-existence of such an output (by returning `⊥`).
3. Or report that it is unable to determine the output.

---

## Key Features
* **Beyond Realizability:** NQSynth natively handles unrealizable specifications without requiring users to manually compute weakest pre-conditions.
* **Zero Rounding Errors:** By restricting inputs, operations, and outputs strictly to rational arithmetic, the generated programs completely avoid the inaccuracies and rounding errors inherent in standard fixed-precision floating-point arithmetic.
* **Expressive Output Programs:** NQSynth generates expressive code constructs, including polynomial term assignments, polynomial constraint-based conditionals, and loops, necessary to resolve arbitrary NRA specifications.

---

## How It Works
NQSynth formalizes a novel synthesis problem: *real program synthesis with rational inputs and outputs* ($\mathcal{RPS_Q}$). 

Depending on the complexity of the specification, the tool relies on robust theoretical foundations and classical number theory:
* **Single-Output Specifications:** NQSynth employs a sound and complete (if terminates) synthesis algorithm utilizing techniques like Real Root Isolation (RRI) and the Rational Root Theorem (RRT).
* **Multi-Output Specifications:** For more complex cases with multiple outputs, NQSynth utilizes a sound synthesis procedure.
* **Quantifier Elimination:** The tool leverages Quantifier Elimination (QE) backends exclusively during the synthesis phase, keeping the synthesized runtime programs dependency-free and efficient.

---

## Installation & Requirements

### System Requirements
* **SageMath** (version >= 10.3)
* **CVC5** (version >= 1.1.2)
* **QEPCAD** backend
* **Python** (version 3.9 recommended via conda)
* **Python Packages**: `z3-solver` (>= 4.13), `sympy` (>= 1.13.1), `pyyaml`

> **_NOTE:_** Our tool works with the above requirements, but it may also work with older versions as well.

### Detailed Installation Steps

1. **Install and Verify CVC5**
   - Download the binary installation from the [CVC5 Releases GitHub repository](https://github.com/cvc5/cvc5/releases).
   - Ensure CVC5 is available in your PATH. To verify the installation, execute:
     ```bash
     cvc5 --sygus-qe-preproc --lang=sygus2 simple_sygus.sy
     ```
     Expected output:
     ```
     (
     (define-fun a_o ((delta_i Real)) Real 0.0)
     )
     ```

2. **Install and Verify SageMath**
   - Setup a dedicated environment using Conda:
     ```bash
     conda config --add channels conda-forge
     conda config --set channel_priority strict
     conda create -n sage sage python=3.9
     conda activate sage
     ```
   - To verify your SageMath installation, run:
     ```bash
     sage simple_qepcad_sage.sage
     ```
     Expected output:
     ```
     delta >= 0 /\ 5000000 pi - 15707963 > 0 /\ 10000000 pi - 31415927 < 0 /\ skoS2 >= 0 /\ skoS2^2 - delta - 2 <= 0 /\ skoS2^2 + delta - 2 >= 0 /\ skoX > 0 /\ skoX - 1 < 0 /\ 1048576 skoX + 1048576 delta - 785407 >= 0 /\ 1048576 skoX - 1048576 delta - 785407 <= 0
     ```

3. **Install Python Packages**
   - Ensure your `sage` environment is active and install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
     *Alternatively:*
     ```bash
     conda install --yes --file requirements.txt
     ```

---

## File Formats

### Input-Output File Format (`--ip_op_vars`)
The input-output definition file is a plain text file. The first line lists all input variables separated by a space, and the second line lists all output variables separated by a space.