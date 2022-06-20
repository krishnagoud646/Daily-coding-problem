"""Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time."""

def best_subsum(array):
    running_sum = 0
    for i in range(1,len(array)):
      #comparing 
        if array[i-1] > 0:
            array[i] +=  array[i-1]
            if array[i] > running_sum: 
               running_sum = array[i]
    return running_sum


array1 = [34, -50, 42, 14, -5, 86]
array2 = [-5, -1, -8, -9]

print(best_subsum(array1))
print(best_subsum(array2))
