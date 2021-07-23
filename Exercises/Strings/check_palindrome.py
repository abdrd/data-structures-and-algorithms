from reverse_without_using_stack import reverse_iterative

# check if a given string is a palindrome without using a deque
def check_palindrome_without_deque(s: str) -> bool:
    # reverse the string
    # and compare the original with reversed version of the string
    # if they are equal, then the string is a palindrome
    s_v2 = reverse_iterative(s)
    for i in range(len(s)):
        if s[i] != s_v2[i]:
            return False
    
    return True

print(check_palindrome_without_deque("radar")) # True
print(check_palindrome_without_deque("radara")) # False
print(check_palindrome_without_deque("kayak")) # True
print(check_palindrome_without_deque("palindrome")) # False