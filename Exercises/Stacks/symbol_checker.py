"""https://runestone.academy/runestone/books/published/pythonds/BasicDS/BalancedSymbolsAGeneralCase.html"""

from s import Stack

# symbol => {    or   [   or   (
def check_symbol_balanced(symbols: str, symbol: str) -> bool:
    assert type(symbols) == str, "give me a string"
    if len(symbols) == 0:
        raise Exception("string is empty")

    CLOSING = ")"

    SYMBOL_CURLY_CLOSING = "}"
    SYMBOL_SQUARE_CLOSING = "]"

    if symbol == "{":
        CLOSING = SYMBOL_CURLY_CLOSING
    elif symbol == "[":
        CLOSING = SYMBOL_SQUARE_CLOSING

    s = Stack()
    balanced = True
    
    for i in range(len(symbols)):
        sym = symbols[i]
        if sym == symbol:
            s.push(sym)
        elif sym == CLOSING:
            if s.is_empty():
                balanced = False
                break
            else:
                s.pop()
    
    return balanced and s.is_empty()

print(check_symbol_balanced("((()", "(")) # False
print(check_symbol_balanced("(())", "(")) # True
print(check_symbol_balanced("{{()}", "{")) # False
print(check_symbol_balanced("{{{()())}}}", "{")) # True
print(check_symbol_balanced("[[]]", "[")) # True
print(check_symbol_balanced("[[[{()}]]", "[")) # False
