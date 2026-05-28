import sys

# Point to the exact site-packages directory found by your search
sys.path.append("/Library/Frameworks/Maple.framework/Versions/2026/Python.APPLE_ARM64_MACOS/lib/python3.11/site-packages")

try:
    import maplesoft.maple as mpl
    import maplesoft.maple.namespace as msymbol
    print("[✓] Step 1: Python bindings imported successfully!")

    # Test 1: Basic Evaluation (Wrapping res in str() to prevent integer stripping crash)
    res = mpl.execute("1 + 1;")
    print(f"[✓] Step 2: Basic calculation works (1 + 1 = {str(res).strip()})")

    # Test 2: Quantifier Elimination Test (Wrapping qe_res in str() as well)
    print("Testing Quantifier Elimination Engine...")
    qe_cmd = "QuantifierElimination:-QuantifierEliminate(exists(x, And(x^2 - 4*y = 0, x > 0)));"
    qe_res = mpl.execute(qe_cmd)
    print(f"[✓] Step 3: Quantifier Elimination works! Result: {str(qe_res).strip()}")

except Exception as e:
    print(f"[X] Testing Failed: {e}")