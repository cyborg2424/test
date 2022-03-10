def sort_list(num: list[int]) -> list[int]:
    n = len(num)
    i = 0
    j = 0

    while i < n-1:
        k = n - i - 1
        j = 0
        while j < k:
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
            j += 1
        i += 1
    return num


print(sort_list([89, 20, 31, 43, 55]))