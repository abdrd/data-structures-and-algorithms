"""
    A palindrome is a string that reads the same forward and backward.
    (toot, radar, madam)

    Check if a string is a palindrome using a DEQUE.
    This is very easy to do using a deque :D

    https://runestone.academy/runestone/books/published/pythonds/BasicDS/PalindromeChecker.html
"""

from dq import Deque

def is_palindrome(word: str) -> bool:
    dq = Deque()

    for c in word:
        dq.add_rear(c)
    
    palindrome = True
    while dq.get_size() > 1 and palindrome:
        # check rear and front characters are the same
        if dq.remove_rear() != dq.remove_front():
            palindrome = False
    return palindrome

print(is_palindrome("madam"))
print(is_palindrome("toot"))
print(is_palindrome("radar"))
print(is_palindrome("woman"))
print(is_palindrome("data"))
print(is_palindrome("structure"))
print(is_palindrome("madama"))
