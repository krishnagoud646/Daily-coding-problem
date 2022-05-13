'''
Input: arr[] = {3, 2, 7, 10}
Output: 13
Explanation: The subsequence is {3, 10}. This gives sum = 13.
This is the highest possible sum of a subsequence following the given criteria
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.


'''


def findMaxSum(arr, n):
    include = 0
    exclude = 0  
    for i in arr:
         
        # Current max excluding i
        new_excl = max (exclude, include)
         
        # Current max including i
        include = exclude + i
        exclude = new_excl
     
    # Return max of include and exclude
    return max(exclude, include)
 
# Driver code
if __name__ == "__main__":
    arr = [5, 1, 1, 5]
    N = 6
     
    # Function call
    print (findMaxSum(arr, N))
