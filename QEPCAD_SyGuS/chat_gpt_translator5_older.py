import sexpdata  # Install via: pip install sexpdata


def indent(mixed_string, start, nesting_count):
    line = mixed_string[start]
    # print("LINE:", line)
    if line[:6] == "return":
        return 1, "    "*nesting_count + line
    if line[:2] == "if":
        n_then, then_string = indent(mixed_string, start+1, nesting_count+1)
        if mixed_string[start+n_then+1][:4] == "else":
            n_else, else_string = indent(mixed_string, start+n_then+2, nesting_count+1)
            return n_then + n_else + 2, "    "*nesting_count + line + "\n" + then_string + "\n" + "    "*nesting_count +mixed_string[start+n_then+1] +"\n" + else_string
        else:
            assert False, "Syntax Error"                
    if line[:4] == "else":
        assert False, "Syntax Error"      
    else:  # non-conditional statement
        n_remaining, remaining_string = indent(mixed_string, start+1, nesting_count)
        return 1+n_remaining, "    "*nesting_count + line + "\n" + remaining_string
        
        
        
def sexp_to_python(expr):
    if isinstance(expr, sexpdata.Symbol):
        return str(expr)
    elif isinstance(expr, (int, float)):
        return str(expr)
    elif isinstance(expr, list):
        if not expr:
            return ''
        op = expr[0]
        if op == sexpdata.Symbol('let'):
            # Handle 'let' expressions
            bindings = expr[1]
            body = expr[2]
            binding_lines = []
            for binding in bindings:
                var_name = str(binding[0])
                var_expr = sexp_to_python(binding[1])
                binding_lines.append(f"{var_name} = {var_expr}")
            body_code = sexp_to_python(body)
            return '\n    '.join(binding_lines + [body_code])
        elif op == sexpdata.Symbol('ite'):
            # Handle 'ite' (if-then-else) expressions
            cond = sexp_to_python(expr[1])
            then_expr = sexp_to_python(expr[2])
            else_expr = sexp_to_python(expr[3])
            return f"if {cond}:\n        return {then_expr}\n    else:\n        return {else_expr}"
        else:
            # Map operators to Python equivalents
            operator_map = {
                '+': '+',
                '-': '-',
                '*': '*',
                '/': '/',
                '>=': '>=',
                '<=': '<=',
                '>': '>',
                '<': '<',
                '=': '==',
                'and': 'and',
                'or': 'or',
                'not': 'not',
            }
            op_str = str(op)
            if op_str in operator_map:
                py_op = operator_map[op_str]
                operands = [sexp_to_python(e) for e in expr[1:]]
                if py_op == 'not':
                    return f'not ({operands[0]})'
                elif py_op in ('and', 'or'):
                    return f'({" {} ".format(py_op).join(operands)})'
                else:
                    return f'({f" {py_op} ".join(operands)})'
            else:
                # Handle function applications or other expressions
                operands = [sexp_to_python(e) for e in expr[1:]]
                return f"{op_str}({', '.join(operands)})"
    else:
        return str(expr)

def tokenize_condition(s):
    token_specification = [
        ('NUMBER',   r'\b\d+(\.\d*)?|\.\d+\b'),  # Integer or decimal number
        ('OP',       r'\*\*|==|!=|<=|>=|<|>|\+|-|\*|/'),  # Operators
        ('KEYWORD',  r'\b(And|Or|Not)\b'),       # Keywords
        ('LPAREN',   r'\('),                     # Left Parenthesis
        ('RPAREN',   r'\)'),                     # Right Parenthesis
        ('COMMA',    r','),                      # Comma
        ('SKIP',     r'[ \t]+'),                 # Skip over spaces and tabs
        ('ID',       r'\b[a-zA-Z_]\w*\b'),       # Identifiers
        ('MISMATCH', r'.'),                      # Any other character
        
    ]
    import re
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line = s.strip()
    pos = 0
    mo = get_token(line)
    tokens = []
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind in ('NUMBER', 'ID', 'OP', 'KEYWORD', 'LPAREN', 'RPAREN', 'COMMA'):
            tokens.append((kind, value))
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} at position {pos}')
        pos = mo.end()
        mo = get_token(line, pos)
    if pos != len(line):
        raise RuntimeError(f'Unexpected character {line[pos]!r} at position {pos}')
    return tokens

class ConditionParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def accept(self, expected_type, expected_value=None):
        if self.current_token is None:
            return False
        if self.current_token[0] != expected_type:
            return False
        if expected_value is not None and self.current_token[1] != expected_value:
            return False
        return True

    def expect(self, expected_type, expected_value=None):
        if not self.accept(expected_type, expected_value):
            raise SyntaxError(f"Expected {expected_type} {expected_value}, got {self.current_token}")
        self.next_token()

    def next_token(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        expr = self.parse_expr()
#        print("parse.expr:",expr)
        if self.current_token is not None:
            raise SyntaxError(f"Unexpected token {self.current_token}")
        return expr

    def parse_expr(self):
        if self.accept('KEYWORD', 'Not'):
            self.next_token()
            self.expect('LPAREN')
            expr = self.parse_expr()
            self.expect('RPAREN')
            return ('Not', expr)
        elif self.accept('KEYWORD', 'And'):
            self.next_token()
            self.expect('LPAREN')
            args = [self.parse_expr()]
            while self.accept('COMMA'):
                self.next_token()
                args.append(self.parse_expr())
            self.expect('RPAREN')
            return ('And', args)
        elif self.accept('KEYWORD', 'Or'):
            self.next_token()
            self.expect('LPAREN')
            args = [self.parse_expr()]
            while self.accept('COMMA'):
                self.next_token()
                args.append(self.parse_expr())
            self.expect('RPAREN')
            return ('Or', args)
        else:
            return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_arith_expr()
        if self.accept('OP'):
            op = self.current_token[1]
            if op in ('==', '!=', '<', '>', '<=', '>='):
                self.next_token()
                right = self.parse_arith_expr()
                return (op, left, right)
        return left

    def parse_arith_expr(self):
        expr = self.parse_term() #('id', name)
        while self.accept('OP', '+') or self.accept('OP', '-'):
            op = self.current_token[1]
            self.next_token()
            right = self.parse_term()
            expr = (op, expr, right)
#            print("parse_arith_expr",expr)
        return expr

    def parse_term(self):
        expr = self.parse_factor() #('id', name)
        while self.accept('OP', '*') or self.accept('OP', '/'):
            op = self.current_token[1]
            self.next_token()
            right = self.parse_factor()
            expr = (op, expr, right)
        return expr

    def parse_factor(self):
        expr = self.parse_power() #('id', name)
        while self.accept('OP', '**'):
            op = self.current_token[1]
            self.next_token()
            right = self.parse_factor()
            expr = (op, expr, right)
        return expr #('id', name)

    def parse_power(self):
        if self.accept('OP', '-'):
            op = self.current_token[1]
            self.next_token()
            expr = self.parse_power()
            return ('neg', expr)
        else:
            return self.parse_atom()

    def parse_atom(self):
        if self.accept('NUMBER'):
            value = self.current_token[1]
            self.next_token()
            return ('number', value)
        elif self.accept('ID'):
            name = self.current_token[1]
            self.next_token()
            return ('id', name+"_i") # adding _i at end of variable names
        elif self.accept('LPAREN'):
            self.next_token()
            expr = self.parse_expr()
            self.expect('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token {self.current_token}")

def condition_ast_to_python(ast):
    if isinstance(ast, tuple):
        op = ast[0]
        if op == 'And':
            return f"({' and '.join(condition_ast_to_python(arg) for arg in ast[1])})"
        elif op == 'Or':
            return f"({' or '.join(condition_ast_to_python(arg) for arg in ast[1])})"
        elif op == 'Not':
            return f"(not {condition_ast_to_python(ast[1])})"
        elif op == 'neg':
            return f"(-{condition_ast_to_python(ast[1])})"
        elif op in ('+', '-', '*', '/', '**'):
            left = condition_ast_to_python(ast[1])
            right = condition_ast_to_python(ast[2])
            return f"({left} {op} {right})"
        elif op in ('==', '!=', '<', '>', '<=', '>='):
            left = condition_ast_to_python(ast[1])
            right = condition_ast_to_python(ast[2])
            return f"({left} {op} {right})"
        elif op == "id":
            return f"{ast[1]}"
        elif op == "number":
            return f"{ast[1]}"
        else:
            raise ValueError(f"Unknown operator {op}")
    elif isinstance(ast, str):
        return ast
    elif isinstance(ast, list):
        return ''.join(condition_ast_to_python(e) for e in ast)
    else:
        node_type, value = ast
        if node_type == 'number':
            return value
        elif node_type == 'id':
            return value
        else:
            raise ValueError(f"Unknown AST node {ast}")

def parse_input1(condition_str):
    tokens = tokenize_condition(condition_str)
#    print("parse_input1.TOKENS:", tokens)
    parser = ConditionParser(tokens)
    ast = parser.parse()
#    print("parse_intput1.ast", ast)
    python_condition = condition_ast_to_python(ast)
    return python_condition



def write_program(pre_condition_sympy, sygus_synthesized_function_file, ip_vars, op_vars, output_program_name):
    # with open(output_program_name, "w+") as f:
    #     print("pass", file=f, flush=True)
    # return

    print(pre_condition_sympy)
    print(sygus_synthesized_function_file)
    print(ip_vars)
    print(op_vars)
    print(output_program_name)

    code_lines = []

    INPUT_1 = pre_condition_sympy

    INPUT_2 = None
    with open(sygus_synthesized_function_file, "r") as f:
        INPUT_2 = f.readlines()[1:-1]
        INPUT_2 = [i.strip().strip("\n").strip() for i in INPUT_2 if re.sub(r'\s+','',i)!=""]
    INPUT_2 = "\n".join(INPUT_2)

    print(INPUT_1)
    print(INPUT_2)


    code_lines.append(f"import sys\n")
    code_lines.append(f"import sympy\n")
    code_lines.append(f"from sympy import *\n")
    
    #create a function for pre-condition:
    # code_lines.append("")
    arguments = ",".join([var+":sympy.Rational" for var in ip_vars])
    code_lines.append("def pre_condition("+arguments+"):\n")
    code_lines.append("    #"+str(pre_condition_sympy) +"\n")


    code_lines.append("\n")
    code_lines.append(f"    pre_cond = {sympy.srepr(pre_condition_sympy)}\n")

    code_lines.append("\n")
    code_lines.append(f"    eval = pre_cond.subs(" + '{' + ", ".join(["\'"+i+"\':"+i for i in ip_vars]) + '})\n')

    code_lines.append("\n")
    code_lines.append(f"    return eval==True\n")

            

        

    for input_var in ip_vars:
        code_lines.append(f"print(\"Enter numerator of {input_var}\")")
        code_lines.append(f"{input_var}_num = int(input())")

        code_lines.append(f"print(\"Enter denominator of {input_var}\")")
        code_lines.append(f"{input_var}_denm = int(input())")
        code_lines.append(f"assert {input_var}_denm!=0")
        code_lines.append(f"{input_var}_i = sympy.Rational({input_var}_num,{input_var}_denm)\n")
    
    
    code_lines.append("if pre_condition(")
    arguments = ",".join([var+"="+var+"_i" for var in ip_vars])
    code_lines[-1] += arguments+")==False:\n"
    code_lines.append('    print("INFEASIBLE!")\n')
    code_lines.append('    sys.exit(1)\n')
    code_lines.append("else:\n")

    #we are doing [1:] because first element is empty after the split
    INPUT_3 = ["(define-fun"+ip for ip in INPUT_2.split("(define-fun")[1:]]
    # print("INPUT2:", INPUT_3)
    count_outputs = len(INPUT_3)

    print("IP3:", INPUT_3)
    input_vars = ip_vars
    # Parse INPUT_1 into a Python condition
    # condition, input_vars = parse_input1(INPUT_1)
    #print("condition_main:", condition)
    # Assemble the final Python code


    # Parse INPUT_2 using sexpdata
    code_return_tuple = "return "
    output_count = 0
    for INPUT_2 in INPUT_3:
        output_count += 1
        parsed = sexpdata.loads(INPUT_2)
        # Remove outermost parentheses if present
        if isinstance(parsed, list) and len(parsed) == 1:
            parsed = parsed[0]
        # Extract function definition
        if parsed[0] == sexpdata.Symbol('define-fun'):
            func_name = str(parsed[1])
            if (output_count > 1):
                code_return_tuple += ", "
            code_return_tuple += func_name
            params = parsed[2]
            param_names = [str(param[0]) for param in params]
            body = parsed[4]
        else:
            raise ValueError("Invalid INPUT_2 format")
        
        # Generate Python code from the S-expression
        body_code = sexp_to_python(body).replace("return if","if")
        #print("____________________")
        # print("body_code:\n", body_code)
        #print("____________________")
        #count_indents = 1
        #body_code_new = body_code.replace(" ","").replace("\t","")
        body_code_split = body_code.split("\n")
        body_code_cleaned = [line.lstrip(' \t') for line in body_code_split]
        s = ""
        
        #flag_else = False
        # stack = [count_indents]
        # # stack_else = []
        # for line in body_code_:
        #     if line[:4] == "else":
        #         # count_indents += 1
        #         c_index = stack[-1]
        #         s += "\n" + "    "*(c_index-1) + line
        #         flag_else = True
            
        #     if line[:3] == "ret":
        #         c_index = stack[-1]
        #         s += "\n" + "    "*c_index + line
        #         if flag_else == True:
        #             stack.pop()
        #             flag_else = False

        #         count_indents -= 1

        #     if line[:2] == "if":
        #         c_index = stack[-1]
        #         s += "\n" + "    "*c_index + line
        #         count_indents += 1
        #         stack.push(count_indents)
        #         flag_else = False

        #     s = s.replace("return","return ")
        # print("____________________")
        # print("______________________body code")
        # print(body_code_cleaned)
        # print("================================")
        
        nLines,indented_code = indent(body_code_cleaned,0,1)

        # print("____________________")
        indented_code = indented_code.replace("return", func_name + " = ")
        # print(indented_code)
        # print("____________________")
        # print("____________________")

        # Indent body_code properly
        # body_code_indented = '    ' + body_code.replace('\n', '\n    ')
        
        # code_lines.append(body_code_indented)
        code_lines.append(indented_code)
    
    # Output the final code
    output_code = '\n'.join(code_lines)
    print("\nGenerated Python program:")
    # print(output_code)
    # code_return_tuple.replace(","," ").split(1:)
    # print(f"    {code_return_tuple}\n")

    with open(output_program_name, "w+") as f:
        print(output_code, file=f, flush=True)
        # print(f"    {code_return_tuple}\n", file=f, flush=True)
        for i in op_vars:
            print(f"    print(\"{i}=\",{i}_o)", file=f, flush=True)
    



def main():
    # Read INPUT_1 and INPUT_2 from the user
    print("Enter INPUT 1 (a quantifier-free non-linear real arithmetic formula):")
    INPUT_1 = input() #"Or ( y_i**2 - 25 <= 0 , Not ( y_i + 2 == 0 ) )" #input()
    # INPUT_1 = " ( y_i + 2 == 0 )" #input()
    #Or ( y_i**2 - 25 <= 0 )
    
    print("\nEnter INPUT 2 (the output of CVC5 as a sygus program):")
    INPUT_2_lines = []
    while True:
        line = input()
        if line.strip() == "(": # leading (
            continue
        if line.strip() == ")": # trailing )
            continue
        if line.strip() == "":
            break
        INPUT_2_lines.append(line)
    INPUT_2 = '\n'.join(INPUT_2_lines)

    #we are doing [1:] because first element is empty after the split
    INPUT_3 = ["(define-fun"+ip for ip in INPUT_2.split("(define-fun")[1:]]
    # print("INPUT2:", INPUT_3)
    count_outputs = len(INPUT_3)

    # Parse INPUT_1 into a Python condition
    condition = parse_input1(INPUT_1)
#    print("condition_main:", condition)
    # Assemble the final Python code
    code_lines = []
    code_lines.append(f"import sys\n")
    code_lines.append(f"if not({condition}):")
    code_lines.append('    print("INFEASIBLE!")')
    code_lines.append('    sys.exit(1)')
    code_lines.append("else:")

    # Parse INPUT_2 using sexpdata
    code_return_tuple = "return "
    output_count = 0
    for INPUT_2 in INPUT_3:
        output_count += 1
        parsed = sexpdata.loads(INPUT_2)
        # Remove outermost parentheses if present
        if isinstance(parsed, list) and len(parsed) == 1:
            parsed = parsed[0]
        # Extract function definition
        if parsed[0] == sexpdata.Symbol('define-fun'):
            func_name = str(parsed[1])
            if (output_count > 1):
                code_return_tuple += ", "
            code_return_tuple += func_name
            params = parsed[2]
            param_names = [str(param[0]) for param in params]
            body = parsed[4]
        else:
            raise ValueError("Invalid INPUT_2 format")
        
        # Generate Python code from the S-expression
        body_code = sexp_to_python(body).replace("return if","if")
#        print("____________________")
#        print("body_code:\n", body_code)
#        print("____________________")
#        count_indents = 1
#        body_code_new = body_code.replace(" ","").replace("\t","")
        body_code_split = body_code.split("\n")
        body_code_cleaned = [line.lstrip(' \t') for line in body_code_split]
        s = ""
#       flag_else = False
        # stack = [count_indents]
        # # stack_else = []
        # for line in body_code_:
        #     if line[:4] == "else":
        #         # count_indents += 1
        #         c_index = stack[-1]
        #         s += "\n" + "    "*(c_index-1) + line
        #         flag_else = True
            
        #     if line[:3] == "ret":
        #         c_index = stack[-1]
        #         s += "\n" + "    "*c_index + line
        #         if flag_else == True:
        #             stack.pop()
        #             flag_else = False

        #         count_indents -= 1

        #     if line[:2] == "if":
        #         c_index = stack[-1]
        #         s += "\n" + "    "*c_index + line
        #         count_indents += 1
        #         stack.push(count_indents)
        #         flag_else = False

        #     s = s.replace("return","return ")
        # print("____________________")
        # print("______________________body code")
        # print(body_code_cleaned)
        # print("================================")
        
        nLines,indented_code = indent(body_code_cleaned,0,1)

        # print("____________________")
        indented_code = indented_code.replace("return", func_name + " = ")
        # print(indented_code)
        # print("____________________")
        # print("____________________")

        # Indent body_code properly
        # body_code_indented = '    ' + body_code.replace('\n', '\n    ')
        
        # code_lines.append(body_code_indented)
        code_lines.append(indented_code)
    
    # Output the final code
    output_code = '\n'.join(code_lines)
    print("\nGenerated Python program:")
    print(output_code)
    print(f"    {code_return_tuple}\n")

if __name__ == "__main__":
    main()
