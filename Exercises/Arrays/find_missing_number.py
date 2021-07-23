# find the missing number in a list of ints
def find_missing(l: list[int]) -> int:
    if len(l) == 0 or len(l) == 1:
        raise Exception("list must contain at least 2 (two) elements")
    l.sort()
    for i in range(len(l) - 1):
        # we came to the end
        if i == len(l) - 1:
            return

        if l[i+1] - l[i] == 2:
            return l[i] + 1

        elif l[i+1] - l[i] > 2:
            return [item for item in range(l[i] + 1, l[i+1])]

print(find_missing([1, 2, 4, 6, 3, 7, 8])) # 5
print(find_missing([1, 2, 3, 5]))          # 4
print(find_missing([1, 2, 3, 8, 9, 10]))   # [4,5,6,7]