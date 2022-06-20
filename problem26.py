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
