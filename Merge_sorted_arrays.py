"""
APPROACH

1) Use the concept of merge sort
2) Take three pointer i,j,k
3) i points to the first element of the first array
4) j points to the first element of the second array
5) k points to the first element of the empty array, where merged sorted array will be stored
6) compare i,j index each time
7) Insert the smaller element in k index and increment k
8) increment the index in which the element is smaller, either i or j
9) repeat the process ,untill i or j reaches length of the array.

"""

def findMinimumInTheArray(array):
    minimum = array[0]
    for i in array:
        if(i<minimum):
            minimum=i
    return minimum

def findMinimumOfTwoNumbers(a,b):
    if(a<b):
        return "i"
    else:
        return "j"

def mergeSortedArrays(array1,array2,mergedArray,m,n):
    i = j = k=0
    while(i!=m and j!=n):
        index = findMinimumOfTwoNumbers(array1[i],array2[j])
        if(index=="i"):
            mergedArray.append(array1[i])
            k+=1
            i+=1
        else:
            mergedArray.append(array2[j])
            k+=1
            j+=1

    print(mergedArray)
    
    if(i==m):
        for l in range(j,n):
            mergedArray.append(array2[l])
            k+=1
    else:
        for l in range(i,m):
            mergedArray.append(array1[l])
            k+=1

    return mergedArray

m,n = map(int,input().split())
array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))
mergedArray = []

print(mergeSortedArrays(array1,array2,mergedArray,m,n))



