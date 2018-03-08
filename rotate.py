def rotate(arr, n):
    x = arr[n - 3]
    for i in range(n - 3, 0, -1):
        arr[i] = arr[i - 1];
    arr[0] = x;
 
arr= [6,7,8,9,10]
n = len(arr)
print ("Given array is:")
for i in range(0, n):
    print (arr[i], end = ' ')
rotate(arr, n)
print ("\nRotated array is:")
for i in range(0, n):
    print (arr[i], end = ' ')
 
