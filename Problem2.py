from itertools import product
# arr = [1,2,3,4,5]
# l = len(arr)
def Product_arr(arr, l):

	i, temp = 1, 1

	product = [1 for i in range(l)]

	for i in range(l):
		product[i] = temp
		temp *= arr[i]
        
	temp = 1

	for i in range(l - 1, -1, -1):
		product[i] *= temp
		temp *= arr[i]

	for i in range(l):
		print(product[i], end = " ")
	return
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split(',')))

    l = len(arr)
    print(Product_arr(arr,l))

# Product_arr(arr, l)
