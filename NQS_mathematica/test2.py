from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl

# Explicitly point to the now-activated Wolfram Kernel
kernel_path = '/Applications/Wolfram Engine.app/Contents/MacOS/WolframKernel'
session = WolframLanguageSession(kernel_path)

try:
    print("Running Quantifier Elimination via Socket Bridge...")
    
    # 1. Define the algebraic symbols
    x, a, b, c = wl.Symbol('x'), wl.Symbol('a'), wl.Symbol('b'), wl.Symbol('c')
    
    # 2. Construct the formula using prefix functions to prevent Python TypeErrors
    # Equivalent to: Exists[x, a*x^2 + b*x + c == 0]
    equation = wl.Equal(
        wl.Plus(
            wl.Times(a, wl.Power(x, 2)),
            wl.Times(b, x),
            c
        ),
        0
    )
    formula = wl.Exists(x, equation)
    
    # 3. Evaluate Resolve via the active ZeroMQ socket session
    # Wrapping it in ToString[..., InputForm] ensures Python receives a clean math string
    result = session.evaluate(wl.ToString(wl.Resolve(formula, wl.Reals), wl.InputForm))
    
    print("\nResult:")
    print(result)

finally:
    # Always close the socket and spin down the background kernel process cleanly
    session.terminate()