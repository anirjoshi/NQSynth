import math
import copy
import sympy as sp
import sympy
from sympy import *
from sympy import Poly
from sympy.abc import x
from sympy import div, QQ
import sys
from sympy import Eq, Ne, Ge, Le, Gt, Lt
import tqdm


def contains_relational_eq_operators(expr):
    """
    Checks if a SymPy expression contains any of the operators:
    <=, >=, !=, ==.

    Parameters:
        expr: SymPy expression.

    Returns:
        True if any of the specified relational operators are present,
        otherwise False.
    """
    # List of relational operator classes to check
    target_operators = {Eq, Ne, Ge, Le}
    
    def _has_operator(expr):
        if expr.is_Relational:
            return type(expr) in target_operators
        elif expr.is_Boolean:
            return any(_has_operator(arg) for arg in expr.args)
        return False

    return _has_operator(expr)


def get_all_polys_expression(sympy_expr):
    polynomials = []
    # If the node is a relational (e.g., Eq, Gt, Lt), skip it
    if sympy_expr.is_Relational:
        polynomials.append(sympy_expr.lhs-sympy_expr.rhs)
        return polynomials
    
    elif isinstance(sympy_expr, (sympy.logic.boolalg.BooleanTrue, sympy.logic.boolalg.BooleanFalse)):
            return []
    else:
        assert sympy_expr.is_Boolean, "ERROR NON_BOOLEAN TERM"
        for arg in sympy_expr.args:
            polynomials += get_all_polys_expression(arg)
    return polynomials




def all_enpoints_different(intervals):
    if len(intervals) <= 1:
        return True
    
    curr_y = intervals[0][1]
    for i in range(1,len(intervals)):
        curr_x = intervals[i][0]
        if curr_x < curr_y:
            print("OVERLAPPING:", curr_x, "<", curr_y, i)
            return False
        curr_y = intervals[i][1]
    # import os
    # os.sleep(0.5)
    return True



def return_factors(num:int):
    num = int(math.sqrt(abs(num)))+1
    factors = []
    for i in range(1,num):
        if num%i==0:
            factors.append(i)
            # factors.append(-i)
    factors.sort()
    return factors


def RRT(polynomial):
    # print(polynomial)
    # print(type(polynomial))
    highest_degree = abs(polynomial.LC().p*polynomial.TC().q)
    lowest_degree = abs(polynomial.TC().p*polynomial.LC().q)
    # print(highest_degree,lowest_degree)
    highest_degree_factor = sympy.divisors(int(highest_degree))
    lowest_degree_factor = sympy.divisors(int(lowest_degree))
    
    # highest_degree_factor = return_factors(highest_degree)
    # lowest_degree_factor = return_factors(lowest_degree)

    all_possible_points = []
    for i in highest_degree_factor:
        for j in lowest_degree_factor:
            # all_possible_points.append(rational(num=i,denm=j))
            # all_possible_points.append(rational(num=-i,denm=j))
            all_possible_points.append(sympy.Rational(j,i))
            all_possible_points.append(sympy.Rational(-j,i))
    
    all_possible_points.append(sympy.Rational(0,1))
    # print(len(all_possible_points))
    return all_possible_points


def RRT_RRI(polynomial, expression_to_satisfy, all_polys_list):
    
    #check rational solutions between intervals
    construct_possible_sols = []
    
    are_endpoints_different = False
    eps = 1/8
    all_intervals = []
    while not(are_endpoints_different):
        # print("EPS:", eps)
        eps = eps/2
        all_intervals = polynomial.intervals(eps=eps)
        all_intervals = [i[0] for i in all_intervals]
        # print(polynomial, all_intervals)
        are_endpoints_different = all_enpoints_different(all_intervals)
    
    assert len(all_intervals)>0

    construct_possible_sols = []
    first_point = all_intervals[0][1] - sympy.Rational(1,1)
    last_point = all_intervals[-1][1] + sympy.Rational(1,1)

    construct_possible_sols.append(first_point)
    construct_possible_sols.append(last_point)
    for i in range(len(all_intervals)-1):
        starti, endi = all_intervals[i]
        nextsi, nextei = all_intervals[i+1]
        construct_possible_sols.append((endi + nextsi)*sympy.Rational(1,2))
    
    univariate_var = expression_to_satisfy.free_symbols
    assert len(univariate_var) == 1
    univariate_var = list(univariate_var)[0]
    
    for point in construct_possible_sols:
        val = expression_to_satisfy.subs({str(univariate_var):point})
        # print(point, val, expression_to_satisfy)
        if val == True:
            return True, point
    
    #check rational solutions NOW for RRT
    construct_possible_sols = []
    for sympy_poly in all_polys_list:
        construct_possible_sols += RRT(polynomial=sympy_poly)
    construct_possible_sols = list(set(construct_possible_sols))

    univariate_var = expression_to_satisfy.free_symbols
    assert len(univariate_var) == 1
    univariate_var = list(univariate_var)[0]
    
    for point in construct_possible_sols:
    # for point in tqdm.tqdm(construct_possible_sols):
        val = expression_to_satisfy.subs({str(univariate_var):point})
        # print(point, val, expression_to_satisfy)
        if val == True:
            return True, point
    

    assert contains_relational_eq_operators(expression_to_satisfy), "SOME BUG IN THE CODE!"
    # assert False, "UNREACHABLE PART OF CODE!"
    return False, None

def get_lambda_val(sympy_expr):
    # return sympy.Rational(0,1)
    # print(sympy_expr)
    polys = get_all_polys_expression(sympy_expr=sympy_expr)
    sympy_polys =[sympy.Poly(p,domain=sympy.polys.domains.QQ) for p in polys]
    
    # print(sympy_polys)

    if len(sympy_polys) == 0:
        return sympy.Rational(0,1)
    
    assert len(sympy_polys) > 0
    product_poly = sympy_polys[0].copy()
    
    for p in sympy_polys[1:]:
        product_poly*=p
    product_poly = sympy.cancel(product_poly)

    print()
    print(product_poly)
    print()
    point = RRT_RRI(product_poly, sympy_expr, sympy_polys)
    return point
    exit(-1)


