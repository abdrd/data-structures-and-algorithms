# check the given string ONLY contains digits
def only_contains_digits(s: str) -> bool:
    if len(s) == 0:
        return False

    str_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for char in s:
        if char not in str_digits:
            return False
    
    return True

print(only_contains_digits("5091836519")) # True
print(only_contains_digits("hello12341")) # False
print(only_contains_digits("578135781561093680a")) # False
print(only_contains_digits("")) # False
