def findSingle( arr, n):
    res = arr[0]
    for i in range(1,n):
        res = res ^ arr[i]
    return res
 
arr = [1,2,3,2,3]
print ("Element occuring only once is", findSingle(arr, len(arr)))
 
