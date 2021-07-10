"""
https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html

Assume the infix expression is a string of tokens delimited by spaces. The operator tokens are *, /, +, and -, along with the left and right parentheses, ( and ). The operand tokens are the single-character identifiers A, B, C, and so on. The following steps will produce a string of tokens in postfix order.

1 - Create an empty stack called opstack for keeping operators. Create an empty list for output.

2 - Convert the input infix string to a list by using the string method split.

3 - Scan the token list from left to right.

4 - If the token is an operand, append it to the end of the output list.

5 - If the token is a left parenthesis, push it on the opstack.

6 - If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.

7 - If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.

8 - When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
"""

from s import Stack
# TODO understand this
def infix_to_postfix(infix_str: str):
    OPERANDS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    OPERATORS = "+-*/"
    PRECEDENCE_DICT = {
        "*": 3,
        "/": 3,
        "-": 2,
        "+": 2,
        "(": 1
    }

    # 1 
    opstack = Stack()
    output = []

    # 2
    token_list = infix_str.split()
    # 3
    for token in token_list:
        # 4
        if token in OPERANDS:
            output.append(token)
        # 5
        elif token == "(":
            opstack.push(token)
        # 6
        elif token == ")":
            popped = opstack.pop()
            while popped != "(":
                output.append(popped)
                popped = opstack.pop()
        # 7
        elif token in OPERATORS:
            #However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
            while (not opstack.is_empty()) and (PRECEDENCE_DICT[opstack.peek()] >= PRECEDENCE_DICT[token]):
                output.append(opstack.pop())
            opstack.push(token)        

    # 8
    while not opstack.is_empty():
        output.append(opstack.pop())

    return " ".join(output)


print(infix_to_postfix("A * B + C * D")) 
print(infix_to_postfix("6 + 3 * 5"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
