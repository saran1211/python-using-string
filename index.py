def linearSearch(arr, n):
	for i in range(n):
		if arr[i] is i:
			return i
	
	return -1

arr = [8,7,6,8,4,6,8,6]
n = len(arr)
print("Fixed Point is " + str(linearSearch(arr,n)))
