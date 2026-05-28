#!/usr/bin/env python3
"""
Reads all .smt files from the synthetic benchmarks directory using Z3's
parse_smt2_file and prints the parsed assertions for each file.
"""

import os
import sys
from z3 import *

def read_and_print_smt_file(filepath):
    """Read a single SMT2 file using Z3 and print its contents."""
    filename = os.path.basename(filepath)
    print("=" * 80)
    print(f"File: {filename}")
    print("=" * 80)

    try:
        assertions = parse_smt2_file(filepath)
        if len(assertions) == 0:
            print("  (no assertions)")
        else:
            assert len(assertions) == 1
            print(assertions[0])
            # for i, a in enumerate(assertions):
            #     print(f"  Assertion {i}: {a}")
    except Z3Exception as e:
        print(f"  Z3 Error: {e}")
    except Exception as e:
        print(f"  Error: {e}")

    print()


def main():
    set_option(max_args=10000000, max_lines=10000000, max_depth=10000000, max_visited=10000000)
    smt_dir = sys.argv[1] if len(sys.argv) > 1 else "synthetic_benchmarks_smt_dir"

    if not os.path.isdir(smt_dir):
        print(f"Error: Directory '{smt_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    smt_files = sorted(
        os.path.join(smt_dir, f)
        for f in os.listdir(smt_dir)
        if f.endswith(".smt")
    )

    if not smt_files:
        print(f"No .smt files found in '{smt_dir}'.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(smt_files)} .smt file(s) in '{smt_dir}'\n")

    found = False

    for filepath in smt_files:
        if "_all_synthetic_benchmarks_collated_4_input16" not in filepath:
            read_and_print_smt_file(filepath)
        else:
            found = filepath
    if found!=False:
        print(f"CHECK THE FILE containing the filename it is ignored for now very large!: {filepath}")
    else:
        print(f"Done. Processed {len(smt_files)} file(s).")


if __name__ == "__main__":
    main()