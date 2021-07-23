# remvoe a given character from a string
def remove_from_str(s: str, char: str) -> str:
    if len(s) == 0 or len(char) == 0:
        raise Exception(":)")

    for c in s:
        if char == c:
            s = s.replace(c, "")
    return s

print(remove_from_str("ali ata bak", "a")) # li t bk
print(remove_from_str("şu köşe yaz köşesi, şu köşe kış köşesi", "ş")) # u köe yaz köesi, u köe kı köesi
print(remove_from_str("that's my butter and bread", "t")) # ha's my buer and bread