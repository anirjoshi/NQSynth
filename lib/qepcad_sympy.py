# sage_to_sympy.py

"""
This script converts a SageMath output string into an equivalent SymPy expression.

Usage:
    python sage_to_sympy.py 'sage_expression_string'

Example:
    python sage_to_sympy.py "0 > -a^100 + x^100 + y^100 /\\ 0 > b^100 - x^100 - y^100"

The script performs the following steps:
- Replaces SageMath logical operators with SymPy equivalents.
- Replaces SageMath exponentiation operator '^' with '**' used in SymPy.
- Parses the modified string into a SymPy expression.
- Outputs the SymPy expression and evaluates it (if variables are assigned values).
"""

import sys
from sympy import symbols, sympify, Eq, And, Or, Not
import re



def test1():
    qepcad_output = "4 r - 4 c^2 - 8 c + 1 < 0 /\\ 2 r - 1 /= 0 /\\ 2 r + 1 /= 0 /\\ [ r^4 + 2 r^3 - 4 c^2 r^2 - 4 c r^2 + r^2 - 4 c r + 5 c^2 < 0 \\/ [ 1280 c^6 + 5120 c^5 + 3776 c^4 - 192 c^3 - 400 c^2 - 64 c - 3 >= 0 /\\ 4 c^2 + 8 c - 3 < 0 ] \\/ [ 1280 c^6 + 5120 c^5 + 3776 c^4 - 192 c^3 - 400 c^2 - 64 c - 3 < 0 /\\ 16 c^4 + 64 c^3 + 40 c^2 - 16 c - 3 > 0 ] \\/ [ 8 c - 3 > 0 /\\ 2 r - 1 > 0 ] \\/ [ 8 c + 1 > 0 /\\ 2 r + 1 < 0 ] \\/ [ 16 c^4 + 64 c^3 + 40 c^2 - 16 c - 3 > 0 /\\ 2 r - 1 > 0 /\\ 2 r^3 + 3 r^2 - 4 c^2 r - 4 c r + r - 2 c > 0 ] \\/ [ 2 r + 1 < 0 /\\ 2 r^3 + 3 r^2 - 4 c^2 r - 4 c r + r - 2 c < 0 ] ]"
    variables = ["r", "c"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output
def test2():
    qepcad_output = "64 r - 144 c + 1 < 0 /\\ 8 r - 1 /= 0 /\\ 8 r + 1 /= 0 /\\ [ 8 r - 1 > 0 \\/ 8 r + 1 < 0 ]"
    variables = ["r", "c"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output

def test3():
    qepcad_output = "r - c^2 - 2 c < 0 /\\ r /= 0 /\\ [ r^2 + 2 c r + r - 2 c < 0 \\/ c + 1 > 0 \\/ r + 1 < 0 \\/ [ c + 3 < 0 /\\ 2 r + 2 c + 1 > 0 ] ]"
    variables = ["r", "c"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output

def test4():
    qepcad_output = "r - 2 c < 0 /\\ r /= 0"
    variables = ["r", "c"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output

def test5():
    qepcad_output = "a - 8 /= 0 /\\ a + 8 /= 0 /\\ b /= 0 /\\ r - 2 /= 0 /\\ r + 2 /= 0 /\\ [ a^4 r^4 - 2 a^4 b^2 r^2 + 128 a^2 b^2 r^2 - 208 a^4 r^2 + a^4 b^4 - 128 a^2 b^4 + 4096 b^4 - 192 a^4 b^2 + 12288 a^2 b^2 + 10816 a^4 < 0 \\/ [ a - 8 > 0 /\\ a^2 r^2 - a^2 b^2 + 64 b^2 - 104 a^2 > 0 ] \\/ [ a + 8 < 0 /\\ a^2 r^2 - a^2 b^2 + 64 b^2 - 104 a^2 > 0 ] \\/ [ a^2 b^2 - 64 b^2 - 100 a^2 > 0 /\\ r - 2 > 0 ] \\/ [ a^2 b^2 - 64 b^2 - 100 a^2 > 0 /\\ r + 2 < 0 ] ]"
    variables = ["r", "c", "b", "a"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output

def test6():
    qepcad_output = "a /= 0 /\\ b - 8 /= 0 /\\ b + 8 /= 0 /\\ r - 2 /= 0 /\\ r + 2 /= 0 /\\ [ b^4 r^4 - 2 a^2 b^4 r^2 - 208 b^4 r^2 + 128 a^2 b^2 r^2 + a^4 b^4 - 192 a^2 b^4 + 10816 b^4 - 128 a^4 b^2 + 12288 a^2 b^2 + 4096 a^4 < 0 \\/ [ b - 8 > 0 /\\ b^2 r^2 - a^2 b^2 - 104 b^2 + 64 a^2 > 0 ] \\/ [ b + 8 < 0 /\\ b^2 r^2 - a^2 b^2 - 104 b^2 + 64 a^2 > 0 ] \\/ [ a^2 b^2 - 100 b^2 - 64 a^2 > 0 /\\ r - 2 > 0 ] \\/ [ a^2 b^2 - 100 b^2 - 64 a^2 > 0 /\\ r + 2 < 0 ] ]"
    variables = ["r", "b", "a"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output
def test7():
    qepcad_output = "a - 9 /= 0 /\\ a + 9 /= 0 /\\ b /= 0 /\\ r - 1 /= 0 /\\ r + 1 /= 0 /\\ [ a^4 r^4 - 2 a^4 b^2 r^2 + 162 a^2 b^2 r^2 - 202 a^4 r^2 + a^4 b^4 - 162 a^2 b^4 + 6561 b^4 - 198 a^4 b^2 + 16038 a^2 b^2 + 10201 a^4 < 0 \\/ [ a - 9 > 0 /\\ a^2 r^2 - a^2 b^2 + 81 b^2 - 101 a^2 > 0 ] \\/ [ a + 9 < 0 /\\ a^2 r^2 - a^2 b^2 + 81 b^2 - 101 a^2 > 0 ] \\/ [ a^2 b^2 - 81 b^2 - 100 a^2 > 0 /\\ r - 1 > 0 ] \\/ [ a^2 b^2 - 81 b^2 - 100 a^2 > 0 /\\ r + 1 < 0 ] ]"
    variables = ["r", "b", "a"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output
def test8():
    qepcad_output = "a /= 0 /\\ b - 9 /= 0 /\\ b + 9 /= 0 /\\ r - 1 /= 0 /\\ r + 1 /= 0 /\\ [ b^4 r^4 - 2 a^2 b^4 r^2 - 202 b^4 r^2 + 162 a^2 b^2 r^2 + a^4 b^4 - 198 a^2 b^4 + 10201 b^4 - 162 a^4 b^2 + 16038 a^2 b^2 + 6561 a^4 < 0 \\/ [ b - 9 > 0 /\\ b^2 r^2 - a^2 b^2 - 101 b^2 + 81 a^2 > 0 ] \\/ [ b + 9 < 0 /\\ b^2 r^2 - a^2 b^2 - 101 b^2 + 81 a^2 > 0 ] \\/ [ a^2 b^2 < 0 \\/ [ 100 b^2 - 81 a^2 > 0 \\/ r - 1 > 0 ] ] \\/ [ a^2 b^2 - 100 b^2 - 81 a^2 > 0 /\\ r + 1 < 0 ] ]"
    variables = ["r", "b", "a"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output

def test9():
    qepcad_output = "[ [ a - 100 /= 0 /\\ a + 10 /= 0 /\\ b /= 0 /\\ r /= 0 /\\ [ a^2 r^2 - 20 a^2 r - a^2 b^2 + 100 b^2 + 100 a^2 < 0 \\/ a^2 r^2 + 20 a^2 r - a^2 b^2 + 100 b^2 + 100 a^2 < 0 \\/ [ a - 10 > 0 /\\ r - 10 > 0 ] \\/ [ a - 10 > 0 /\\ r + 10 < 0 ] \\/ [ a + 10 < 0 /\\ r - 10 > 0 ] \\/ [ a + 10 < 0 /\\ r + 10 < 0 ] ] ] ]"
    variables = ["r", "b", "a"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    return qepcad_output

def test10():
    qepcad_output = "a /= 0 /\\ b - 10 = 0 /\\ b + 10 /= 0 /\\ r /= 0 /\\ [ b^2 r^2 - 20 b^2 r - a^2 b^2 + 100 b^2 + 100 a^2 < 0 \\/ b^2 r^2 + 20 b^2 r - a^2 b^2 + 100 b^2 + 100 a^2 < 0 \\/ [ b - 10 > 0 /\\ r - 10 > 0 ] \\/ [ b - 10 > 0 /\\ r + 10 < 0 ] \\/ [ b + 10 < 0 /\\ r - 10 > 0 ] \\/ [ b + 10 < 0 /\\ r + 10 < 0 ] ]"
    variables = ["r", "b", "a"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output


def test11():
    qepcad_output = "delta >= 0 /\\ [ skoS + 1 > 0 \\/ skoS^6 + 4 skoS^5 - 12 skoS^4 + 2 skoS^3 + 92 skoS^2 + 32 skoS - 7 > 0 ]"
    variables = ["delta", "skoS"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output


def test12():
    qepcad_output = "[ [ delta >= 0 ] ]"
    variables = ["delta", "skoS"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output


def test13():
    qepcad_output = "TRUE"
    variables = ["delta", "skoS"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output


def test14():
    qepcad_output = "FALSE"
    variables = ["delta", "skoS"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output

def test15():
    qepcad_output = "[[~0 > -a^100 + x^100 + y^100] /\\ 0 = b^100 - x^100 - y^100]"
    variables = ["delta", "skoS"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output

def test16():
    qepcad_output = "M g + delta + 1 >= 0 /\ M g - delta + 1 <= 0 /\ S g m + delta + 1 >= 0 /\ S g m - delta + 1 <= 0 /\ [ [ delta - 1 > 0 /\ delta g m - S g m + g m - delta + 1 <= 0 ] \/ [ delta g m - S g m + g m - delta + 1 <= 0 /\ delta g m + S g m - g m - delta - 1 <= 0 ] \/ [ delta g m - S g m + g m - delta + 1 > 0 /\ delta g m + S g m - g m + delta - 1 >= 0 ] ]"
    variables = ["M", "g","delta","S","C","m"]
    #vars = {str(var):Real(str(var)) for var in variables}
    #vars["And"] = And
    #vars['Or'] =  Or
    #vars['Not'] = Not
    # vars['RealVal'] = RealVal
    # print("HERE")
    # z3_expr = sage_z3_parser_python(qepcad_output)
    # return z3_expr, vars
    return qepcad_output

def sage_to_sympy(sage_expr_str):
    """
    Converts a SageMath output string into a SymPy expression.

    Parameters:
    sage_expr_str (str): The SageMath expression string.

    Returns:
    sympy.Expr: The equivalent SymPy expression.
    """
    
    # Replace square brackets with parentheses
    sage_expr_str = sage_expr_str.replace('[', '(').replace(']', ')')

    # Replace exponentiation operator '^' with '**'
    sage_expr_str = sage_expr_str.replace('^', '**')

    # Replace logical operators
    replacements = {
        r'/\\': ' & ',    # Logical AND
        r'\\/': ' | ',    # Logical OR
        r'~': '~',        # Logical NOT (unchanged)
    }

    # Replace relational operator '/=' with '!='
    sage_expr_str = sage_expr_str.replace('/=', '!=')

    # Apply replacements for logical operators
    for sage_op, sympy_op in replacements.items():
        sage_expr_str = sage_expr_str.replace(sage_op, sympy_op)

    # Insert explicit multiplication operators where necessary
    # Patterns to handle:
    # - Number followed by variable or open parenthesis: 2x -> 2*x, 2(x+1) -> 2*(x+1)
    # - Variable followed by variable or open parenthesis: x y -> x*y, x(y+1) -> x*(y+1)
    # - Close parenthesis followed by variable or number: (x+1)y -> (x+1)*y
    # - Exponent followed by variable: x**2 y -> x**2 * y

    # Remove extra spaces
    sage_expr_str = re.sub(r'\s+', ' ', sage_expr_str)
    expr = sage_expr_str
    # Insert multiplication symbols between numbers and variables
    expr = re.sub(r'(\d+)\s+([_a-zA-Z][_a-zA-Z0-9]*)', r'\1*\2', expr)
    expr = re.sub(r'([_a-zA-Z][_a-zA-Z0-9]*)\s+(\d+)', r'\1*\2', expr)
    expr = re.sub(r'([_a-zA-Z][_a-zA-Z0-9]*)\s+([_a-zA-Z][_a-zA-Z0-9]*)', r'\1*\2', expr)


    sage_expr_str = expr

    # Insert * between a number and a variable or open parenthesis
    sage_expr_str = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', sage_expr_str)
    # Insert * between a variable and a variable or open parenthesis
    sage_expr_str = re.sub(r'([a-zA-Z\)])([a-zA-Z(])', r'\1*\2', sage_expr_str)
    # Insert * between a close parenthesis and a number or variable
    sage_expr_str = re.sub(r'(\))(\d|\w)', r'\1*\2', sage_expr_str)
    # Insert * between a number or variable and an open parenthesis
    sage_expr_str = re.sub(r'(\w|\d)(\()', r'\1*\2', sage_expr_str)
    # Insert * between exponentials and variables
    sage_expr_str = re.sub(r'(\*\*\d+)([a-zA-Z])', r'\1*\2', sage_expr_str)

    # Ensure proper spacing around operators for sympify
    sage_expr_str = re.sub(r'([<>!=]=?)', r' \1 ', sage_expr_str)
    sage_expr_str = re.sub(r'([&|~()])', r' \1 ', sage_expr_str)
    sage_expr_str = re.sub(r'\s+', ' ', sage_expr_str)

    # Extract variable names
    variables = set(re.findall(r'[a-zA-Z]\w*', sage_expr_str))
    # symbols_dict = {var: symbols(var) for var in variables}
    # local_dict = symbols_dict
    # sympy_expr = sympify(sage_expr_str, locals=local_dict)
    expr = sage_expr_str
    expr = expr.replace("/\\", " & ")
    expr = expr.replace("\\/", " | ")
    sage_expr_str = expr

    # Define the variables used in the expression
    symbols_dict = {var: symbols(var) for var in variables}
    local_dict = symbols_dict
    
    sage_expr_str = "( " + sage_expr_str + " )"
    print(local_dict)
    print(sage_expr_str)

    # Parse the expression into a SymPy expression
    try:
        sympy_expr = sympify(sage_expr_str, locals=local_dict)
    except Exception as e:
        print("Error parsing the expression:")
        print(e)
        sys.exit(1)

    return sympy_expr


def parse_qepcad_exprs(expr):
    pattern = r'(!=)|(==)|(>=)|(<=)|(<)|(>)'
    
    if "!=" in expr:
        result = expr.split("!=")
        assert len(result) == 2
        result = f"Ne({result[0]},{result[1]})"
    elif "==" in expr:
        result = expr.split("==")
        assert len(result) == 2
        result = f"Eq({result[0]},{result[1]})"
    elif "<=" in expr:
        result = expr.split("<=")
        assert len(result) == 2
        result = f"Le({result[0]},{result[1]})"
    elif ">=" in expr:
        result = expr.split(">=")
        assert len(result) == 2
        result = f"Ge({result[0]},{result[1]})"
    elif "<" in expr:
        result = expr.split("<")
        assert len(result) == 2
        result = f"Lt({result[0]},{result[1]})"
    elif ">" in expr:
        result = expr.split(">")
        assert len(result) == 2
        result = f"Gt({result[0]},{result[1]})"
    else:
        result = expr
    
    return result




def sage_to_sympy2(expr, variables = None, file_name = None):
    assert "~" not in expr
    expr = expr.replace("==","=")
    expr = expr.replace("/=","!=")
    # expr = expr.replace("TRUE", "True")
    # expr = expr.replace("FALSE", "False")
    expr = expr.replace("TRUE", "true")
    expr = expr.replace("FALSE", "false")

    # if expr == "TRUE":
    #     return "True"
    # if expr == "FALSE":
    #     return "False"
    # print("HHHHHHHHHhhhhhHHHHHHHH")
    # Replace logical symbols with Python logical operators
    variables = set(re.findall(r'[a-zA-Z]\w*', expr))
    symbols_dict = {var: symbols(var) for var in variables if var!="true" and var!="false"}
    local_dict = symbols_dict

    expr = expr.replace("/\\", " @AND@ ")
    expr = expr.replace("\\/", " @OR@ ")
    expr = expr.replace("[", "(")
    expr = expr.replace("]", ")")
    expr = expr.replace("{", "(")
    expr = expr.replace("}", ")")
    expr = expr.replace("^", "**")
    expr = expr.replace("TRUE", "sympy.logic.boolalg.BooleanTrue")
    expr = expr.replace("FALSE", "sympy.logic.boolalg.BooleanFalse")
    print("EXPR:", expr)


    # Remove extra spaces
    expr = re.sub(r'\s+', ' ', expr)

    # Insert multiplication symbols between numbers and variables
    expr_old = None
    while expr_old != expr:
        expr_old = expr
        expr = re.sub(r'(\d+)\s+([_a-zA-Z][_a-zA-Z0-9]*)', r'\1 * \2', expr)
        expr = re.sub(r'([_a-zA-Z][_a-zA-Z0-9]*)\s+(\d+)', r'\1 * \2', expr)
        expr = re.sub(r'([_a-zA-Z][_a-zA-Z0-9]*)\s+([_a-zA-Z][_a-zA-Z0-9]*)', r'\1 * \2', expr)
    # expr = re.sub(r'([_a-zA-Z][_a-zA-Z0-9]*)\s+([_a-zA-Z][_a-zA-Z0-9]*)', r'\1 * \2', expr)
    # expr = re.sub(r'([_a-zA-Z][_a-zA-Z0-9\*]*)\s+([_a-zA-Z][_a-zA-Z0-9\*]*)', r'\1*\2', expr)
    print("EXPR:",expr)
    # exit(-1)
    expr_list = expr.split()
    expr_list = [i if i.replace(" ","")!="=" else "==" for i in expr_list ]
    expr_list = [i if i.replace(" ","")!="/=" else "!=" for i in expr_list ]
    
    # exit(-1)
    assert len(expr_list) > 0
    new_expr_list = [expr_list[0]]
    bool_operations = ["(",")", "@AND@", "@OR@"]
    i = 1
    while i < len(expr_list):
        expr1 = expr_list[i]
        if expr1 in bool_operations:
            new_expr_list.append(expr1)
        elif i > 0 and new_expr_list[-1] in bool_operations:
            new_expr_list.append(expr1)
        else:
            new_expr_list[-1] += " " + (expr1)
            # i+=1
        i += 1
    # exit(-1)
    #check that ( can only have ( or @AND or @OR to the left or its the starting
    #check that ) can only have ) or @AND or @OR to the right or its the ending
    expr_list = new_expr_list
    i = 0
    while i < len(expr_list):
        if expr_list[i] == "(":
            assert i == 0  or \
                    expr_list[i-1] in ["(", "@AND@", "@OR@"]

        if expr_list[i] == ")":
            assert i == len(expr_list)-1  or \
                    expr_list[i+1] in [")", "@AND@", "@OR@"]
        i+=1
    # exit(-1)
    # expr_list = ["("] + expr_list + [")"]

    expr_list = [parse_qepcad_exprs(expr) for expr in expr_list]
    print("expr_list_modified:", expr_list)

    default_op = "And"
    expr_list = expr_list

    assert len(expr_list) > 0
    # print(expr_list[0])
    # assert expr_list[0] not in bool_operations
    assert expr_list[0] not in ["@AND@", "@OR@"]
    # stack_exprs = [[expr_list[0]]]
    # stack_operation = [default_op]

    stack_exprs = [[]]
    stack_operation = [default_op]

    last_exp = ""

    i = 0
    while i < len(expr_list):
        # print()
        # print("STACK_EXPR:", stack_exprs)
        # print(expr_list)
        # print(i, expr_list[i], stack_exprs, stack_operation)
        c_expr = expr_list[i]
        if c_expr == ")":
            assert len(stack_exprs) > 0
            
            last_op = stack_operation.pop()
            # if last_op == None:
            # last_op = default_op
    
            last_exp_list = stack_exprs.pop()
            assert len(last_exp_list) > 0
            if len(last_exp_list) == 1:
                last_exp = last_exp_list[0]
            else:
                # print("last_exp_list:",last_exp_list)
                last_exp = last_op + "(" + ", ".join(last_exp_list) + ")"
            # print(stack_exprs)
            # assert len(stack_exprs) > 0
            if len(stack_exprs) > 0:
                stack_exprs[-1].append(last_exp)            
            else:
                stack_exprs.append(last_exp)
                stack_operation.append(default_op)
        
        elif c_expr == "(":
            stack_exprs.append([])
            stack_operation.append(default_op)
            

        elif c_expr in ["@AND@","@OR@"]:
            if c_expr == "@AND@":
                stack_operation[-1] =  "And"
            else:
                stack_operation[-1] =  "Or"

        else:
            # print("SE:", stack_exprs)
            # c_expr = "( " + c_expr + " )"
            stack_exprs[-1].append(c_expr)
        i+=1
    
    stack_exprs = [expr for expr in stack_exprs if expr!=[]]

    # print("stack_operation:",stack_operation)
    # print("stack_exprs:",stack_exprs)


    assert len(stack_exprs) == 1
    if stack_operation[-1] == "@OR@":
        stack_operation[-1] = "Or"
    else:
        stack_operation[-1] = "And"
    
    if len(stack_exprs[0]) == 1:
        final_formula = "( " + stack_exprs[0][0] + " )"
    else:
        final_formula = stack_operation[-1] + "( " + ", ".join(stack_exprs[-1]) + " )"
    print("FINAL:FORMULA:", final_formula ,local_dict) 
    import sympy
    sympy_expr = sympy.sympify(final_formula, locals=local_dict)
    # import sympy
    print(isinstance(sympify,sympy.logic.boolalg.BooleanTrue))
    print(type(sympy_expr))
    print("SYMPY_EXPR_INSIDE:", sympy_expr)
    # exit(-1)
    # print()
    # print("FF:", final_formula)
    return sympy_expr
    return final_formula
    # if variables != None:
        
    #     z3_vars = {str(var): z3.Real(str(var)) for var in variables}
    #     z3_vars["And"] = And
    #     z3_vars["Or"] = Or 
    #     z3_vars['Not'] = Not
    #     z3_vars['RealVal'] = RealVal
    #     parsed_content = eval(final_formula, z3_vars)


    #     if file_name != None:
    #         set_pp_option('max_visited', 10000000)
    #         sj = Solver()
    #         sj.add(parsed_content)
    #         file_content = sj.to_smt2()
    #         with open(file_name, "w") as f:
    #             f.write(file_content)
    #         return file_content
    #     else:
    #         return parsed_content

    # else:
    #     return final_formula



def main():
    # if len(sys.argv) != 2:
    #     print("Usage: python sage_to_sympy.py 'sage_expression_string'")
    #     sys.exit(1)

    tests=[ test2,test1, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13,test14, test16]
    # tests = [test16]
    # sage_expr_str = sys.argv[1]
    for test in tests:
        sage_expr_str = test()
        sympy_expr = sage_to_sympy2(sage_expr_str)

        print("NORMAL EXPRESSION:")
        print(sage_expr_str)
        print("SymPy Expression2:")
        print(sympy_expr)
        import sympy
        # print(sympy.srepr(sympy_expr))

        print("============================")

        from sympy_z3 import convert_sympy_z3
        convert_sympy_z3(sympy_expr)

        print("_________________________________")

        # exit(-1)
    # Optionally, evaluate the expression by assigning values to the variables
    # Example:
    # result = sympy_expr.subs({'a': 2, 'b': 3, 'x': 1, 'y': 1})
    # print("Evaluated Expression:")
    # print(result)

if __name__ == "__main__":
    main()
