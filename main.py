def fun_enumeration(array, x): # O(n^2)
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[i] + array[j+1] == x:
                return [array[i], array[j+1]]
    return []


def fun_with_set(array, x): #O(n)
    hash_set = set()
    for i in array:
        if x - i in hash_set:
            return [i, x - i]
        hash_set.add(i)
    return []


def binary_search(array, x): #O(n log n)
    for i in range(len(array)):
        l = i + 1
        r = len(array) - 1
        find = x - array[i]
        while l <= r:
            mid = l + (r-l) // 2
            if array[mid] == find:
                return [array[mid], array[i]]
            if array[mid] > find:
                r = mid - 1
            else:
                l = mid + 1
    return []


def two_pointer(array, x): #O(n)
    l = 0
    r = len(array) - 1
    while l < r:
        if array[l] + array[r] == x:
            return [array[l], array[r]]
        if array[l] + array[r] == x:
            l += 1
        else:
            r -= 1
    return []


lst = [2, 3, 4, 5, 7]
k = 6
print(fun_enumeration(lst, k))

print(fun_with_set(lst, k))

print(binary_search(lst, k))

print(two_pointer(lst, k))
