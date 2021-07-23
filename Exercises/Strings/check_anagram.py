def check_anagram(s: str, s2: str) -> bool:
    if len(s) == 0 or len(s2) == 0:
        return False
    if len(s) != len(s2):
        return False
    
    for i in range(0, len(s) - 1):
        if s[i] not in s2:
            return False

    return True 


print(check_anagram("fired", "fried")) # True
print(check_anagram("again", "aigna")) # True
print(check_anagram("boat", "oabt")) # True
print(check_anagram("", "hello")) # False
print(check_anagram("hello", "")) # False
print(check_anagram("howdoyouturnthison", "robinhood")) # False
print(check_anagram("plane", "water")) # False