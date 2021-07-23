def number_of_words(s: str) -> int:
    if len(s) == 0:
        return 0
        
    return len(s.split(" "))


print(number_of_words("hello guys"))
print(number_of_words("i feel great"))
print(number_of_words("how are you doing?"))
print(number_of_words(""))