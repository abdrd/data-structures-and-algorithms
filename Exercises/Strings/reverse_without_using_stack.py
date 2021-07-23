# reverse a string without using a stack

def reverse_iterative(s: str) -> str:
    if len(s) == 0:
        return ""
    
    res = ""

    for i in range(0, len(s)):
        res += s[(len(s) - 1) - i]
    
    return res

#print(reverse_iterative("hello, how are you doing?"))
#print(reverse_iterative(":) :( :) :( D: :D"))

def reverse_recursive(s: str) -> str:
    if len(s) == 0:
        return ""
    
    return s[-1] + reverse_recursive(s[:-1])

print(reverse_recursive("hello, how are you doing?"))
print(reverse_recursive(":) :( :) :( D: :D"))