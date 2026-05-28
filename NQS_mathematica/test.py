import subprocess
import shutil

def wolfram_resolve(formula_str, domain="Reals"):
    """
    Performs Quantifier Elimination using the native wolframscript CLI tool.
    Dynamically locates the executable to avoid path errors.
    """
    # 1. Ask Python to find where macOS installed wolframscript
    script_path = shutil.which('wolframscript')
    
    # Fallback to the standard Mac installation path if Anaconda hides it
    if not script_path:
        script_path = '/usr/local/bin/wolframscript'
        
    wolfram_cmd = f"ToString[Resolve[{formula_str}, {domain}], InputForm]"
    
    # 2. Run wolframscript
    process = subprocess.Popen(
        [script_path, "-code", wolfram_cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate()
    
    # 3. Handle errors and capture hidden stdout crash logs
    if process.returncode != 0:
        error_msg = (
            f"WolframScript crashed with code {process.returncode}.\n"
            f"--- STDOUT (Hidden Errors) ---\n{stdout.strip()}\n"
            f"--- STDERR ---\n{stderr.strip()}"
        )
        raise RuntimeError(error_msg)
        
    return stdout.strip()

# --- Main Logic ---
if __name__ == "__main__":
    print("Running Quantifier Elimination...")
    
    # Construct the formula in pure Wolfram Language syntax string
    formula = "Exists[x, a * x^2 + b * x + c == 0]"
    
    try:
        result = wolfram_resolve(formula, domain="Reals")
        print("\nResult:")
        print(result)
    except Exception as e:
        print(f"\nAn error occurred: {e}")