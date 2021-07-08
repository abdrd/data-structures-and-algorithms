"""
Use stacks to write an algorithm to check if the given string of parentheses are balanced.

BALANCED PARENTHESES EXAMPLES:
    (define ... (* 3 4) (if ... ...))
    ((())() ())
UNBALANCED PARENTHESES:
    ((())
    ()())

The challenge is to write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced. To solve this problem we need to make an important observation. As you process symbols from left to right, the most recent opening parenthesis must match the next closing symbol. Also, the first opening symbol processed may have to wait until the very last symbol for its match. Closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out. This is a clue that stacks can be used to solve the problem.

https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimpleBalancedParentheses.html

"""

#from Python.Stack.List_Based.stack_v2 import Stack 
from s import Stack

def check_paren(paren_string: str) -> bool:
    assert type(paren_string) == str, "give me a string"
    if len(paren_string) == 0:
        raise Exception("string is empty")

    s = Stack()
    balanced = True
    
    # go over the entire string
    for i in range(len(paren_string)):
        # get the current char
        symbol = paren_string[i]
        # store opening parens
        if symbol == "(":
            s.push(symbol)
        # if we find a closing paren
        elif symbol == ")":
            # if the stack is empty, that means there are no opening parens
            # thus, we cannot match our closing paren with an opening paren
            if s.is_empty():
                balanced = False
                break
            # there is at least 1 opening paren.
            # we pop that opening paren because we matched it with our closing paren.
            else:
                s.pop()
    
    return balanced and s.is_empty()

one = check_paren("(((def x ...))(") # False"
two = check_paren("()(* 3 4)()") # True
three = check_paren("((())((()))") # False
#four = check_paren("") # Exception
five = check_paren("(((())") # False
#six = check_paren(1) # AssertionError

print(one)
print(two)
print(three)
#print(four)
print(five)
#print(six)

print(check_paren("(((())))")) # True
print(check_paren("(")) # False
print(check_paren(")")) # False
print(check_paren("())()")) # False
