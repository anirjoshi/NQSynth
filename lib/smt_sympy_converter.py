import sympy
from sympy import symbols, Eq, Ne, Lt, Le, Gt, Ge, And, Or, Not, Implies, Add, Mul, Integer, Rational, pi
import z3
# from z3 import *
import os
import sys

def tokenize(s):
    """Tokenize the input s-expression string into a list of tokens."""
    tokens = []
    token = ''
    i = 0
    while i < len(s):
        c = s[i]
        if c in '()':
            if token:
                tokens.append(token)
                token = ''
            tokens.append(c)
            i += 1
        elif c.isspace():
            if token:
                tokens.append(token)
                token = ''
            i += 1
        else:
            token += c
            i += 1
    if token:
        tokens.append(token)
    return tokens

def parse(tokens):
    """Parse the tokens into an abstract syntax tree (AST)."""
    if not tokens:
        return None
    token = tokens.pop(0)
    if token == '(':
        lst = []
        while tokens[0] != ')':
            lst.append(parse(tokens))
            if not tokens:
                raise ValueError('Unmatched "("')
        tokens.pop(0)  # Pop the closing ')'
        return lst
    elif token == ')':
        raise ValueError('Unexpected ")"')
    else:
        return token

def get_symbol_value(symbols_stack, name):
    # print()
    # print("SYMBOL STACK:", symbols_stack)
    # print()
    """Retrieve a symbol's value from the symbols stack."""
    for symbols in reversed(symbols_stack):
        if name in symbols:
            return symbols[name]
    return None

def set_symbol_value(symbols_stack, name, value):
    """Set a symbol's value in the current scope."""
    symbols_stack[-1][name] = value

def process_ast(ast, symbols_stack):
    """Process the AST and convert it into a SymPy expression."""
    if isinstance(ast, list):
        if not ast:
            return None
        head = ast[0]
        if head == 'let':
            # Handle 'let' expressions
            bindings_list = ast[1]
            body = ast[2]
            # Push a new scope
            symbols_stack.append({})
            # Process bindings
            for binding in bindings_list:
                var_name = binding[0]
                var_expr = binding[1]
                var_value = process_ast(var_expr, symbols_stack)
                set_symbol_value(symbols_stack, var_name, var_value)
            # Process body
            result = process_ast(body, symbols_stack)
            # Pop the scope
            symbols_stack.pop()
            return result
        else:
            # Process expressions
            operator = head
            args = ast[1:]
            sympy_args = [process_ast(arg, symbols_stack) for arg in args]
            return process_operator(operator, sympy_args)
    else:
        # Handle literals and variables
        value = get_symbol_value(symbols_stack, ast)
        # print("ANI_VAL:",value, ast)
        if value is not None:
            return value
        elif ast.lstrip('-').replace('.', '', 1).isdigit():
            # Handle integers and decimals
            return sympy.sympify(ast, rational=True)
        else:
            # Create a new symbol
            new_symbol = sympy.Symbol(ast)
            set_symbol_value(symbols_stack, ast, new_symbol)
            return new_symbol

def process_operator(operator, args):
    """Map Z3 s-expression operators to SymPy equivalents."""
    if operator == '+':
        return Add(*args)
    elif operator == '-':
        if len(args) == 1:
            return -args[0]
        else:
            return args[0] - args[1]
    elif operator == '*':
        return Mul(*args)
    elif operator == '/':
        # print("ANI:120:", sympy.Rational(args[0],args[1]))
        return sympy.Rational(args[0],args[1]) #/ args[1]
    elif operator == 'div':
        return sympy.Rational(args[0],args[1])
        # return args[0] // args[1]
    elif operator == 'mod':
        return args[0] % args[1]
    elif operator == '=':
        return Eq(args[0], args[1])
    elif operator == 'distinct':
        return Ne(args[0], args[1])
    elif operator == '>':
        return Gt(args[0], args[1])
    elif operator == '<':
        return Lt(args[0], args[1])
    elif operator == '>=':
        return Ge(args[0], args[1])
    elif operator == '<=':
        return Le(args[0], args[1])
    elif operator == 'and':
        return And(*args)
    elif operator == 'or':
        return Or(*args)
    elif operator == 'not':
        return Not(args[0])
    elif operator == '=>':
        return Implies(args[0], args[1])
    elif operator == 'xor':
        return sympy.Xor(*args)
    elif operator == 'to_real':
        return sympy.nsimplify(args[0], rational=True)
    elif operator == 'to_int':
        return sympy.floor(args[0])
    elif operator == 'abs':
        return sympy.Abs(args[0])
    elif operator == 'sqrt':
        return sympy.sqrt(args[0])
    elif operator == 'pow':
        return args[0] ** args[1]
    else:
        # Handle unknown operators
        if hasattr(sympy, operator):
            func = getattr(sympy, operator)
            return func(*args)
        else:
            raise ValueError(f'Unknown operator: {operator}')

def sexpr_to_sympy(sexpr_str):
    """Convert a Z3 s-expression string into SymPy expressions."""
    tokens = tokenize(sexpr_str)
    # print("TOKENS:", tokens)

    ast = parse(tokens)
    assert tokens == [], f"Not all tokens consumed {ast}"
    # print("AST:", ast)
    symbols_stack = [{}]
    expr = process_ast(ast, symbols_stack)
    # Collect all symbols from the symbol stack
    symbols_dict = {}
    for symbols in symbols_stack:
        symbols_dict.update(symbols)
    return symbols_dict, expr

def get_variables(expr):
    """
    Get all variables (symbols) from a SymPy expression, excluding those with specified prefixes.

    Parameters:
    expr (sympy expression): The SymPy expression from which to extract variables.
    exclude_prefixes (list of str): List of prefixes to exclude from the variables.

    Returns:
    set: A set of sympy.Symbol objects representing the variables in the expression.
    """
    # if exclude_prefixes is None:
    #     exclude_prefixes = []
    all_vars = expr.free_symbols
    # filtered_vars = {var for var in all_vars}
    return all_vars

if __name__ == '__main__':
    ip_dir_name = sys.argv[1]
    # print(os.listdir(ip_file_name))
    # exit(-1)
    for file in sorted(os.listdir(ip_dir_name)):
        # continue
        if (".smt" not in file):# or ("0029" not in file):
            continue
        ip_file_name = ip_dir_name + "/" + file
        print(ip_file_name)
        post_condition = z3.And(z3.parse_smt2_file(ip_file_name))
        sexpr_str = post_condition.sexpr()

        # Convert to SymPy
        symbols_dict, sympy_expr = sexpr_to_sympy(sexpr_str)

        
        # print('Symbols:',symbols_dict.items() )
        # for name, symbol in symbols_dict.items():
        #     print(f'{name}: {symbol}')
        print("SEXPR:", sexpr_str)
        print('SymPy Expression:')
        print(sympy_expr)
        # print(help(sympy_expr))
        print("SYMBOLS:", sympy_expr.free_symbols)
        print()
        print("Sexpr:",sympy.srepr(sympy_expr))
        tmp = symbols("tmp")
        # sympy_expr = sympy_expr & (tmp == 0)
        # print()
        # print(sympy_expr)
        print("Sexpr:",sympy.srepr(sympy_expr))
        # print()
        # print(sympy_expr.subs('tmp',sympy.Rational(0,1)))

        """CODE TO CONVERT SEXPR FROM SYMPY TO QEPCAD"""
        if sympy_expr.free_symbols == set():
            continue
        from sympy_qepcad import convert_sympy_to_qepcad
        sage_conv = convert_sympy_to_qepcad(sympy.srepr(sympy_expr))
        print("CONVERTED SAGE:" )
        for sym in sympy_expr.free_symbols:
            print(f"{sym} = var(\'{sym}\')")
        print("qf = qepcad_formula")
        print("tmp = var('tmp')")
        print()
        print(sage_conv)
        """CODE FINISHES HERE!!!!"""

        



        # vars= []
        # for var in sympy_expr.free_symbols:
            # vars.append(z3.Real(str(var)))
        # print(eval(str(sympy_expr)))

        print("______________________________________")
        # exit(-1)
    exit(-1)
    # Example s-expression with 'let' expressions
    sexpr_str = '''(let ((a!1 (* skoS (+ (- 4.0) (* skoS (+ 2.0 skoS)))))
          (a!3 (* skoCOSS (+ (- 2.0) (* skoCOSS (- 2.0)))))
          (a!4 (* skoCOSS (+ (- 10.0) (* skoCOSS (- 2.0)))))
          (a!5 (* skoS (+ (- 6.0) (* skoCOSS (- 6.0)) (* skoS (- 2.0)))))
          (a!7 (not (<= (* pi (/ 1.0 2.0)) skoS))))
(let ((a!2 (* skoSINS
                  (+ (- 3.0) (* skoCOSS (- 2.0)) a!1 (* skoSINS (+ 1.0 skoS))))))
(let ((a!6 (<= a!2 (+ 2.0 a!3 (* skoS (+ a!4 a!5))))))
      (and (<= 0.0 delta)
           (not a!6)
           a!7
           (not (<= pi (/ 15707963.0 5000000.0)))
           (not (<= (/ 31415927.0 10000000.0) pi))))))'''

    # Convert to SymPy
    symbols_dict, sympy_expr = sexpr_to_sympy(sexpr_str)
    tmp = symbols("tmp")
    sympy_expr = sympy_expr & (tmp <= 0)
    print('Symbols:')
    for name, symbol in symbols_dict.items():
        print(f'{name}: {symbol}')
    print('\nSymPy Expression:')
    print(sympy_expr)
    print()
    print(sympy_expr.subs('tmp',sympy.Rational(0,1)))
