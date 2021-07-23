# return the occurence of a given character in a string
def occured_n_times(s: str, char: str) -> int:
    if len(char) > 1 or len(char) == 0:
        raise Exception("char length must be 1")
    res = 0
    if len(s) == 0:
        return res
    
    for c in s:
        if c == char:
            res += 1
        
    return res

print(occured_n_times("hello", "l")) #  2
print(occured_n_times("today is the day ", "a")) # 2
print(occured_n_times("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbcccccc", "a")) # idk
print(occured_n_times("", "a")) # 0
#print(occured_n_times("something", "")) # Exception
#print(occured_n_times("something again", "again")) # Exception

