'''Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.'''
arr = [1, 2, 0] 
arr_size=len(arr)
def naive_method(arr): 
    arr.sort()

    smallest = 1
    for i in range(arr):
        if i <= 0:
            continue
        elif i== smallest:
            smallest+=1
    return smallest


def hash_method(arr): 
    hash_dict = {}
    def helper(arr):
        for i in range(arr):
            if i <=0:
                continue
            else:
                hash_dict[i] = True

    helper(arr)
    i = 1
    while True:
        if i not in hash_dict:
            return i
        i+=1


def findMissingPositive(arr):
    start,end= 0, 0 

    def segregate(arr): 
        nonlocal end
        for i in range(arr_size):
            if arr[i] > 0:
                arr[end], arr[i] = arr[i], arr[end]
                end+=1

    segregate(arr)
    print(arr)
    print(end)
    for i in range(start,end):
        if abs(arr[i]) <= end:
            if arr[abs(arr[i])-1] > 0: 
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    print(arr)
    for i in range(start,end):
        if arr[i] > 0:
            return i+1

    return end+1


print("The smallest positive missing number is ",findMissingPositive(arr))

