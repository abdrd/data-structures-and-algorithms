# find minimum and maximum elements in a list of ints
def find_min_max(l: list) -> dict[str, int]:
    if len(l) == 0:
        raise Exception("list cannot be empty")

    min = l[0]
    max = l[0]
    for el in l:
        if el < min:
            min = el
        if el > max:
            max = el
    
    return {"min": min, "max": max}

print(find_min_max([65,124,56,316,16,13,61,4721,71,61])) # min: 13, max: 4721
print(find_min_max([13671763171, -123516, 1, 100, 613])) # min: -123516, max: 13671763171
