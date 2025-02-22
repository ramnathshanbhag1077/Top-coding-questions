#Given an array and an element, remove all the occurrences of that element from the array
#Loop through 
n = int(input())
array = list(map(int,input().split()))
val = int(input())

finalArray=[]
occurences = 0
length = 0
for i in array:
    if(i!=val):
        finalArray.append(i)
        length+=1
    else:
        occurences+=1

for j in range(0,len(finalArray)):
    array[j]=finalArray[j]

print(length)
print(finalArray)