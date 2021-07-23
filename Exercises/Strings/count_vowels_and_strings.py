# count vowels and consonants
def count_vowels_and_consonants(s: str) -> dict[str, int]:
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxyz"

    res = {
        "vowels": 0,
        "consonants": 0
    }

    if len(s) == 0:
        return res

    for char in s:
        if char in vowels:
            res["vowels"] += 1
        elif char in consonants:
            res["consonants"] += 1

    return res 

print(count_vowels_and_consonants("white clouds over the mountain")) # vowels: 11, consonants: 15 
print(count_vowels_and_consonants("jjkdjgkdjgkdjgkhjgkd")) # vowels: 0
print(count_vowels_and_consonants("aiouyiouaeu")) # consonants: 0
print(count_vowels_and_consonants("")) # 0 0
