# find the kth largest and kth smallest number in an array of ints
def find(l: list[int], k: int):
    if k < 0 or k > len(l) - 1:
        raise Exception("k out of range")
    # i havent learned about sorting algorithms yet, so i am using the built-in one
    l.sort()
    return {"kth_smallest": l[k - 1], "kth_largest": l[-(k)]}

print(find([12, 315, 61, 717, 1234, 891, 11, -1], 3)) # kth_smallest: 12, kth_largest: 717
print(find([41, 51,5613 ,661, 901, 124, -125, 71, 0, -156, 2000], 2)) # kth_smallest: -125, kth_largest: 2000 