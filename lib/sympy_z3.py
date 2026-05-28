from sympy import *
import sympy
import z3

def sympy_to_z3(expr, z3_vars):
    if expr.is_Number:
        # print("ANI:", expr, expr.is_Integer, expr.is_Rational)
        #this is made false here because doesn't seem to work with false
        # and anyways in our procedure we convert into theory of Reals
        if False and expr.is_Integer:
            print("INT:", expr)
            return z3.IntVal(int(expr))
        elif expr.is_Rational:
            # print("RATIONA::", expr)
            return z3.RealVal(float(expr))
        else:
            # print("REAL:", expr)
            return z3.RealVal(float(expr))
    elif expr.is_Symbol:
        name = expr.name
        if name not in z3_vars:
            if expr.is_integer:
                z3_vars[name] = z3.Int(name)
            else:
                z3_vars[name] = z3.Real(name)
        return z3_vars[name]
    elif expr.is_Add:
        args = [sympy_to_z3(arg, z3_vars) for arg in expr.args]
        return z3.Sum(args)
    elif expr.is_Mul:
        args = [sympy_to_z3(arg, z3_vars) for arg in expr.args]
        result = args[0]
        for arg in args[1:]:
            result = result * arg
        return result
    elif expr.is_Pow:
        base, exp = expr.args
        base_z3 = sympy_to_z3(base, z3_vars)
        exp_z3 = sympy_to_z3(exp, z3_vars)
        return base_z3 ** exp_z3
    elif expr.is_Relational:
        lhs = sympy_to_z3(expr.lhs, z3_vars)
        rhs = sympy_to_z3(expr.rhs, z3_vars)
        if expr.rel_op == '==':
            return lhs == rhs
        elif expr.rel_op == '!=':
            return lhs != rhs
        elif expr.rel_op == '<':
            return lhs < rhs
        elif expr.rel_op == '<=':
            return lhs <= rhs
        elif expr.rel_op == '>':
            return lhs > rhs
        elif expr.rel_op == '>=':
            return lhs >= rhs
    elif expr.func == sympy.And:
        args = [sympy_to_z3(arg, z3_vars) for arg in expr.args]
        return z3.And(args)
    elif expr.func == sympy.Or:
        args = [sympy_to_z3(arg, z3_vars) for arg in expr.args]
        return z3.Or(args)
    elif expr.func == sympy.Not:
        arg = sympy_to_z3(expr.args[0], z3_vars)
        return z3.Not(arg)
    elif expr.func == sympy.Abs:
        arg = sympy_to_z3(expr.args[0], z3_vars)
        return z3.If(arg >= 0, arg, -arg)
    elif isinstance(expr, sympy.logic.boolalg.BooleanTrue):
        return z3.BoolVal(True)
    elif isinstance(expr, sympy.logic.boolalg.BooleanFalse):
        return z3.BoolVal(False)
    else:
        raise NotImplementedError(f"Unhandled sympy expression: {expr}")

def convert_sympy_z3(expr):
    print("Expr:", expr)
    # sympy_classes = {name: getattr(sympy, name) for name in dir(sympy) if not name.startswith('_')}
    # expr = sympy.simplify(expr, sympy_classes)
    z3_vars = {}
    z3_expr = sympy_to_z3(expr, z3_vars)
    print(z3_expr.sexpr())
    s = z3.Solver()
    s.add(z3_expr)
    print("Z3 Solver:")
    print(s)
    if s.check() == z3.sat:
        print("Satisfiable")
        print("Model:")
        print(s.model())
    else:
        print("Unsatisfiable")


def main():
    srepr_str = input("Enter srepr expression: ")
    # Define the mapping of names to sympy classes
    sympy_classes = {name: getattr(sympy, name) for name in dir(sympy) if not name.startswith('_')}
    # Reconstruct the sympy expression
    # print(sympy_classes)
    y = sympy.var("sympy_var_y")
    x = sympy.var("sympy_var_x")
    polys = []
    polys.append((x*x*x*x + y*y*y - 2 < 0))
    polys.append((x*x*x + y*y*y*y - 2 > 0))
    polys.append((x*x + y*y - 8 < 0))
    expr = sympy.simplify(sympy.And(polys[0], polys[1], polys[2]))
    # expr = sympy.simplify(srepr_str, sympy_classes)
    print(expr)
    # exit(-1)
    # Convert sympy expression to z3 expression
    z3_vars = {}
    z3_expr = sympy_to_z3(expr, z3_vars)
    print("z3_vars:", z3_vars)
    # Create a z3 Solver instance
    s = z3.Solver()
    s.add(z3_expr)
    print(z3_expr.sexpr())
    # Now s is the z3 Solver instance with the expression added
    # For demonstration, print the solver
    print("Z3 Solver:")
    print(s)
    # Also, we can check the satisfiability
    if s.check() == z3.sat:
        print("Satisfiable")
        print("Model:")
        print(s.model())
    else:
        print("Unsatisfiable")

if __name__ == '__main__':
    main()
