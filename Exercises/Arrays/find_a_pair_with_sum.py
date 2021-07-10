"""
Given an unsorted integer array, find a pair with the given sum in it.
For example:
    Input:
    
    arr = [8, 7, 2, 5, 3, 1]
    sum = 10
    
    Output:
    
    Pair found (8, 2)
    or
    Pair found (7, 3)
    
    
    Input:
    
    arr = [5, 2, 6, 8, 1, 9]
    sum = 12
    
    Output: Pair not found
"""
# * O(n^2) Quadratic time complexity
def find_pair(l: list[int], sum: int) -> list[tuple[int]]:
    assert len(l) > 1, "list must contain at least 2 elements"

    res = []

    for i in range(len(l)):
        assert type(l[i]) == int, "all ints!"
        if i == len(l) - 1:
            break
        for j in range(i+1, len(l)):
            if l[i] + l[j] == sum:
                res.append((l[i], l[j]))

    return res

print(find_pair([8, 7, 2, 5, 3, 1], 10))
print(find_pair([1, 2, 3, 0, -1, 4], 3))
print(find_pair([3, 4, 5, 12, 61, 71], 61))