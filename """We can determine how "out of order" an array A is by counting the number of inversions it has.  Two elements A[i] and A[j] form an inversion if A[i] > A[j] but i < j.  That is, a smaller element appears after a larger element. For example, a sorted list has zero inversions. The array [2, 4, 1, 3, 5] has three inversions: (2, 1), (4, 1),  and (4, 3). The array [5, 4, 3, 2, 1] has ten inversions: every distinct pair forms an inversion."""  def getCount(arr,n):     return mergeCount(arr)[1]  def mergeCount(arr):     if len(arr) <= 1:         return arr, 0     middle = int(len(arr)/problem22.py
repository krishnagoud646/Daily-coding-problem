"""We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.
For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), 
and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion."""

def getCount(arr,n):
    return mergeCount(arr)[1]

def mergeCount(arr):
    if len(arr) <= 1:
        return arr, 0
    middle = int(len(arr) / 2)
    left, a = mergeCount(arr[:middle])
    right, b = mergeCount(arr[middle:])
    result, c = mergeSplitCount(left, right)
    return result, (a + b + c)

def mergeSplitCount(left, right):
    result = []
    count = 0
    i,j = 0,0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count   

arr = [5, 4, 3, 2, 1] 
n = len(arr) 
print("Number of inversions are", getCount(arr,n)) 
