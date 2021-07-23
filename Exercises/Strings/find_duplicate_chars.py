"""
    given a string, return the duplicate characters
"""

from typing import List, Set


def find_dups(s: str) -> list[str]:
    if len(s) == 0:
        return []

    dups = set()
    chars = set()

    for c in s:
        if c in chars:
            dups.add(c)
            continue
        chars.add(c)

    return dups

print(find_dups("they are good")) # [e, o]
print(find_dups("sakkijarven polkka")) # [a, k]        