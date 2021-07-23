# reverse an array 
def reverse_array(arr: list) -> list:
    start = 0
    end = len(arr) - 1

    while start < end:
        # arr[start] = arr[end]
        # arr[end] = arr[start]
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
    return arr

print(reverse_array([1,2,3,4,5,6,7]))
print(reverse_array(["A", "B", "C", "D", "E", "F"]))
print(reverse_array([]))