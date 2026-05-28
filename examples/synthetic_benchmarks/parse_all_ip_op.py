#!/usr/bin/env python3
"""
Reads all .smt files from the synthetic benchmarks directory using Z3's
parse_smt2_file and prints the parsed assertions for each file.
"""

import os
import sys
# from z3 import *

def read_and_ip_op_vars(filepath):
    """Read a single SMT2 file using Z3 and print its contents."""
    filename = os.path.basename(filepath)
    print("=" * 80)
    print(f"File: {filename}")
    print("=" * 80)

    try:
        with open(filepath, "r") as f:
            readlines = f.readlines()
        print(readlines)
    except Exception as e:
        print(f"  Error: {e}")

    print()


def main():

    smt_dir = sys.argv[1] if len(sys.argv) > 1 else "synthetic_benchmarks_smt_dir"

    if not os.path.isdir(smt_dir):
        print(f"Error: Directory '{smt_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    smt_files = sorted(
        os.path.join(smt_dir, f)
        for f in os.listdir(smt_dir)
        if f.endswith(".txt")
    )

    if not smt_files:
        print(f"No .txt files found in '{smt_dir}'.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(smt_files)} .smt file(s) in '{smt_dir}'\n")

    for filepath in smt_files:
        if "_all_synthetic_benchmarks_collated_4_input16" not in filepath:
            read_and_ip_op_vars(filepath)

    print(f"Done. Processed {len(smt_files)} file(s).")


if __name__ == "__main__":
    main()