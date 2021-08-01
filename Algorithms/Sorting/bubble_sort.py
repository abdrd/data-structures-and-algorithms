def bubble_sort(l: list[int]) -> list[int]:
    n = len(l)
  
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] > l[j + 1] :
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print(bubble_sort([4, 15, 621, 8, 1, 0, -1]))