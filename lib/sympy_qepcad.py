# sympy_to_qepcad.py
"""
This script converts a SymPy srepr string to a SageMath QEPCAD input formula.

Usage:
    python sympy_to_qepcad.py 'srepr_string'

Example:
    python sympy_to_qepcad.py "Exists([Symbol('x')], Eq(Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))), Integer(1)))"

Note:
    The script uses 'eval' to reconstruct the SymPy expression from the srepr string.
    For security reasons, only use this script with trusted input.

"""

import sys
from sympy import *
import sympy
# Updated import statement based on SymPy version
# from sympy.logic.quantifiers import Exists, ForAll

def sympy_expr_to_qepcad(expr, additional_tmp_var = "tmp"):
    """
    Converts a SymPy expression to a QEPCAD formula string.

    Parameters:
    expr (sympy.Expr): The SymPy expression to convert.

    Returns:
    str: The QEPCAD formula string.
    """
    if isinstance(expr, Symbol):
        return str(expr)
    elif isinstance(expr, (Integer, Rational)):
        return str(expr)
    elif isinstance(expr, Add):
        args = [sympy_expr_to_qepcad(arg) for arg in expr.args]
        return "("+' + '.join(args)+")"
    elif isinstance(expr, Mul):
        args = [sympy_expr_to_qepcad(arg) for arg in expr.args]
        return "("+' * '.join(args)+")"
    elif isinstance(expr, Pow):
        base = sympy_expr_to_qepcad(expr.base)
        exp = sympy_expr_to_qepcad(expr.exp)
        return f'(({base})**{exp})'
    elif isinstance(expr, Eq):
        lhs = sympy_expr_to_qepcad(expr.lhs)
        rhs = sympy_expr_to_qepcad(expr.rhs)
        return f'({lhs} == {rhs})'
    elif isinstance(expr, Ne):
        lhs = sympy_expr_to_qepcad(expr.lhs)
        rhs = sympy_expr_to_qepcad(expr.rhs)
        return f'({lhs} != {rhs})'
    elif isinstance(expr, Lt):
        lhs = sympy_expr_to_qepcad(expr.lhs)
        rhs = sympy_expr_to_qepcad(expr.rhs)
        return f'({lhs} < {rhs})'
    elif isinstance(expr, Le):
        lhs = sympy_expr_to_qepcad(expr.lhs)
        rhs = sympy_expr_to_qepcad(expr.rhs)
        return f'({lhs} <= {rhs})'
    elif isinstance(expr, Gt):
        lhs = sympy_expr_to_qepcad(expr.lhs)
        rhs = sympy_expr_to_qepcad(expr.rhs)
        return f'({lhs} > {rhs})'
    elif isinstance(expr, Ge):
        lhs = sympy_expr_to_qepcad(expr.lhs)
        rhs = sympy_expr_to_qepcad(expr.rhs)
        return f'({lhs} >= {rhs})'
    elif isinstance(expr, And):
        args = [sympy_expr_to_qepcad(arg) for arg in expr.args]
        return "qf.and_(" + ', '.join(args) + ")"
    elif isinstance(expr, Or):
        args = [sympy_expr_to_qepcad(arg) for arg in expr.args]
        return ' qf.or_(' + ', '.join(args) + ")"
    elif isinstance(expr, Not):
        arg = sympy_expr_to_qepcad(expr.args[0])
        return f'qf.not_({arg})'
    elif isinstance(expr, Implies):
        lhs = sympy_expr_to_qepcad(expr.args[0])
        rhs = sympy_expr_to_qepcad(expr.args[1])
        return f'qf.or_( qf.not_({lhs}), {rhs} )'
    # elif isinstance(expr, Exists):
    #     vars = ', '.join([str(var) for var in expr.variables])
    #     body = sympy_expr_to_qepcad(expr.function)
    #     return f'ex {vars}, ( {body} )'
    # elif isinstance(expr, ForAll):
    #     vars = ', '.join([str(var) for var in expr.variables])
    #     body = sympy_expr_to_qepcad(expr.function)
    #     return f'all {vars}, ( {body} )'
        
    else:
        assert not(isinstance(expr,sympy.logic.boolalg.BooleanFalse)), f"ERROR: {expr} as a boolean FALSE type"
        # return f"qf.and_({additional_tmp_var}==0, {additional_tmp_var}==1)"
        assert not(isinstance(expr,sympy.logic.boolalg.BooleanTrue)), f"ERROR: {expr} as a boolean TRUE type"
        # return f"qf.not_(qf.and_({additional_tmp_var}==0, {additional_tmp_var}==1))"
        raise ValueError(f'Unsupported expression type: {type(expr)}')


def convert_sympy_to_qepcad(srepr:str):
    allowed_names = {}
    for module in [sympy.core, sympy.functions, sympy.logic.boolalg, sympy.logic, sympy]:
        allowed_names.update({name: getattr(module, name) for name in dir(module) if not name.startswith('_')})
    # print()
    # for i in allowed_names:
    #     print(i)    #print(allowed_names)
    # print()
    expr = eval(srepr, {"__builtins__": None}, allowed_names)
    # print(expr)
    # print()
    qepcad_formula = sympy_expr_to_qepcad(expr)
    return qepcad_formula

def main():
    if len(sys.argv) != 2:
        print("Usage: python sympy_to_qepcad.py 'srepr_string'")
        sys.exit(1)

    srepr_string = sys.argv[1]

    # Reconstruct the SymPy expression from the srepr string
    # WARNING: Using eval can be unsafe. Only use with trusted input.
    allowed_names = {}
    for module in [sympy.core, sympy.functions, sympy.logic.boolalg, sympy.logic, sympy]:
        allowed_names.update({name: getattr(module, name) for name in dir(module) if not name.startswith('_')})
    # print()
    # for i in allowed_names:
    #     print(i)    #print(allowed_names)
    # print()
    expr = eval(srepr_string, {"__builtins__": None}, allowed_names)
    print(expr)
    print()
    qepcad_formula = sympy_expr_to_qepcad(expr)

    print("QEPCAD Input Formula:")
    print(qepcad_formula)

if __name__ == "__main__":
    main()
